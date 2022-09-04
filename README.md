# Decode SOURCEDEFENDER
## Intro
SOURCEDEFENDER is a tool to obfuscate, limit and encrypt python code.

It uses a combination of python-minifier, tgcrypto.ctr256_encrypt and base64.a85encode
to keep users from inspecting or modifying the original code.

The code in this project tries to go this route in reverse
base64.a85decode and tgcrypto.ctr256_decrypt to get a potentially minified version of the original code.

## Technical

SOURCEDEFENDER itself seems to be built in Cython and is internally called pyx

<https://pypi.org/project/sourcedefender/>

Most of the code interesting to decode packed projects seems to be in loader.cpython-310-x86_64-linux-gnu.so
One of the largest functions in that file is __pyx_pw_6loader_8_loader__15load