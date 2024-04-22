# https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper/blob/main/scripts/ch_lib/util.py
# -*- coding: UTF-8 -*-
import os
import io
import hashlib

# print for debugging
def printD(msg):
    print(f"Civitai Helper: {msg}")

def read_chunks(file, size=io.DEFAULT_BUFFER_SIZE):
    """Yield pieces of data from a file-like object until EOF."""
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        yield chunk

# Now, hashing use the same way as pip's source code.
def gen_file_sha256(filname):
    printD("Use Memory Optimized SHA256")
    blocksize=1 << 20
    h = hashlib.sha256()
    length = 0
    with open(os.path.realpath(filname), 'rb') as f:
        for block in read_chunks(f, size=blocksize):
            length += len(block)
            h.update(block)

    hash_value =  h.hexdigest()
    printD("sha256: " + hash_value)
    printD("sha256: " + hash_value[0:10])
    printD("length: " + str(length))
    return hash_value

if __name__ == "__main__":
    gen_file_sha256('C:/Stable-diffusion/models/Stable-diffusion/realisticVisionV51_v51VAE.safetensors')