# Decode SOURCEDEFENDER

SOURCEDEFENDER is a tool to obfuscate, limit and encrypt python code.

It uses a combination of base64.a85encode, tgcrypto.ctr256_decrypt and python-minifier
to keep users from inspecting or modifying the original code.