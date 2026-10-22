#!/usr/bin/env python3
"""Bind saved MobSF JSON artifacts to an APK and evaluate a score threshold."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import sys
import tempfile
from datetime import datetime, timezone


def digest_file(path):
    md5 = hashlib.md5(usedforsecurity=False)
    sha256 = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            md5.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha256.hexdigest()


def read_object(path):
    value = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value, dict) or 'error' in value:
        raise ValueError(f'{path.name}: expected a successful MobSF JSON object')
    return value


def record(args):
    if not 0 <= args.threshold <= 100:
        raise ValueError('threshold must be between 0 and 100')
    if not args.mobsf_version.strip():
        raise ValueError('MobSF version must not be empty')
    apk = args.apk.resolve(strict=True)
    report = read_object(args.report)
    card = read_object(args.scorecard)
    md5, sha256 = digest_file(apk)
    if card.get('hash') != md5:
        raise ValueError('scorecard hash does not match APK MD5')
    if report.get('md5') != md5 or report.get('sha256') != sha256:
        raise ValueError('report MD5/SHA-256 do not match APK')
    score = card.get('security_score')
    if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score) or not 0 <= score <= 100:
        raise ValueError('scorecard security_score must be a number between 0 and 100')
    findings = {}
    for severity in ('high', 'warning', 'info', 'secure', 'hotspot'):
        entries = card.get(severity)
        if not isinstance(entries, list):
            raise ValueError(f'scorecard {severity} must be a list')
        findings[severity] = entries
    changes = args.changes_file.read_text(encoding='utf-8').strip()
    if not changes:
        raise ValueError('changes file must describe applied changes or explicitly state none')
    evidence = {
        'recorded_at': datetime.now(timezone.utc).isoformat(),
        'apk': str(apk), 'bytes': apk.stat().st_size,
        'md5': md5, 'sha256': sha256,
        'mobsf_version': args.mobsf_version,
        'security_score': score, 'threshold': args.threshold,
        'meets_score_threshold': score >= args.threshold,
        'changes': changes, 'findings': findings,
        'limitations': 'Saved-report threshold check only; suppression state, scanner integrity, signing, scan freshness, and device behavior require separate verification.',
    }
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    bundle = output.with_name(output.stem + '-reports')
    if output.exists() or bundle.exists():
        raise ValueError('output or report bundle already exists; choose a new output path')
    # Private permissions: raw reports can contain credentials and business data.
    old_umask = os.umask(0o077)
    temporary = None
    created_bundle = False
    try:
        bundle.mkdir(mode=0o700)
        created_bundle = True
        for source, name in ((args.report, 'report.json'), (args.scorecard, 'scorecard.json')):
            with source.open('rb') as src, (bundle / name).open('xb') as dst:
                shutil.copyfileobj(src, dst)
        evidence['raw_reports'] = str(bundle)
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=output.parent, delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(evidence, stream, indent=2, allow_nan=False)
            stream.write('\n')
        # Exclusive link avoids overwriting evidence created concurrently.
        os.link(temporary, output)
    except BaseException:
        if created_bundle:
            shutil.rmtree(bundle)
        raise
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        os.umask(old_umask)
    print(f'MobSF score {score}/100; target {args.threshold}; evidence: {output}')
    return 0 if evidence['meets_score_threshold'] else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apk', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--scorecard', type=Path, required=True)
    parser.add_argument('--mobsf-version', required=True)
    parser.add_argument('--changes-file', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--threshold', type=int, default=70)
    args = parser.parse_args()
    try:
        return record(args)
    except (ValueError, OSError) as exc:
        print(f'Cannot record evidence: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
