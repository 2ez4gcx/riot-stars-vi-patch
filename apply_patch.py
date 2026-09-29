#!/usr/bin/env python3
"""Ap ban va Viet hoa Riot Stars len dia goc, co kiem sha256 truoc va sau.

Chay:  python apply_patch.py <dia_goc.bin> [riot-stars-vi.rsvi] [dia_ra.bin]
       Mac dinh tao "Riot Stars (VN).bin" + .cue canh dia goc.
Chi can Python 3, khong can cai them gi.  Khong sua dia goc.
"""
import hashlib
import os
import struct
import sys
import zlib

SEC = 2352


def msf(lba):
    """dia chi sector dang BCD (phut, giay, khung) - co 150 khung dau dia"""
    lba += 150
    bcd = lambda v: ((v // 10) << 4) | (v % 10)
    return bytes([bcd(lba // 4500), bcd(lba // 75 % 60), bcd(lba % 75)])


def viet_cue(dst):
    cue = os.path.splitext(dst)[0] + '.cue'
    dong = ['FILE "%s" BINARY' % os.path.basename(dst), '  TRACK 01 MODE2/2352', '    INDEX 01 00:00:00']
    with open(cue, 'wb') as f:
        f.write(('\r\n'.join(dong) + '\r\n').encode('utf-8'))
    return cue


def main(src, patch, dst):
    raw = open(patch, 'rb').read()
    if raw[:5] != b'RSVI1':
        sys.exit('Khong phai file va Riot Stars (.rsvi).')
    p = zlib.decompress(raw[5:])
    nb, sha_goc, sha_dich, size_goc = struct.unpack_from('<I32s32sQ', p, 0)
    pos = struct.calcsize('<I32s32sQ')
    a = open(src, 'rb').read()
    if len(a) != size_goc or hashlib.sha256(a).digest() != sha_goc:
        sys.exit('Dia goc khong dung (kich thuoc hoac sha256 khong khop).\n'
                 'Can file .bin Mode2/2352 mot track cua Riot Stars (SLPS-00829), xem README.')
    out = bytearray(nb * SEC)
    sync = b'\x00' + b'\xff' * 10 + b'\x00'
    n_map, = struct.unpack_from('<I', p, pos); pos += 4
    for _ in range(n_map):
        d0, cnt, s0 = struct.unpack_from('<IIi', p, pos); pos += 12
        for k in range(cnt):
            d = d0 + k
            o = d * SEC
            out[o:o + 12] = sync
            out[o + 12:o + 15] = msf(d)
            out[o + 15] = 2
            if s0 >= 0:
                s = s0 + k
                out[o + 16:o + SEC] = a[s * SEC + 16:(s + 1) * SEC]
    n_diff, = struct.unpack_from('<I', p, pos); pos += 4
    for _ in range(n_diff):
        d, off, ln = struct.unpack_from('<IHH', p, pos); pos += 8
        o = d * SEC + 16 + off
        out[o:o + ln] = p[pos:pos + ln]
        pos += ln
    h = hashlib.sha256(out).digest()
    open(dst, 'wb').write(out)
    print('da tao %s' % dst)
    print('da tao %s' % viet_cue(dst))
    print('sha256 dia ra: %s' % h.hex())
    print('KHOP ban phat hanh' if h == sha_dich else 'KHONG KHOP - hay bao loi kem sha256 dia goc')


if __name__ == '__main__':
    if not 2 <= len(sys.argv) <= 4:
        sys.exit(__doc__)
    src = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    patch = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, 'riot-stars-vi.rsvi')
    dst = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(src)),
                                                              'Riot Stars (VN).bin')
    main(src, patch, dst)
