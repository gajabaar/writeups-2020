## Intro

**Points:** 50

**Category**: `Crypto`

**Challenge Description**:

> Alice sent over a couple of images with sensitive information to Bob, encrypted with a pre-shared key. It is the most secure encryption scheme, theoretically...

**Associated Files**:

[image1.png](image1.png)

![image1.png](image1.png)

[image2.png](image2.png)

![image2.png](image2.png)

## Background

Since this is a `crypto` challenge, it is safe to assume that the two images are the result of an encryption scheme. The challenge description tells us that these are two different images encrypted using the same encryption key. As for the encryption scheme itself, nothing is known except the fact that it is the most secure one, theoretically. So the best guess, given the information and the points associated with the challenge, is that the encryption scheme is `one-time-pad`. Theoretically, this is an unbreakable cipher.

In this encryption scheme, each byte of the plain-text is encrypted with a corresponding byte of the encryption key (known as the `pad`). The length of the key is the same as that of the message. It is called *one-time* pad because the `pad` is not to be used to encrypt multiple plain-texts. This is because hidden patterns or similarities are revealed if we reuse the key.

If the plain-texts are m_1 and m_2 and the pad used is p. Then the ciphertexts are given by:

![$$m_1 \oplus p = c_1\\m_2 \oplus p = c_2$$](one-time-pad.png)

Now if we xor the ciphertexts themselves, we get;

![$c_1 \oplus c_2 = m_1 \oplus p \oplus m_2 \oplus p = m_1 \oplus m_2$](exploit.png)

This is true because the xor operation is both commutative and associative. As we can see, the xor of ciphertexts and that of the plain-texts follow the same pattern. And due to the nature of the xor operation, if any bit in the result of xor-ing plain-texts or cipher-texts is the same, it must mean that those bytes are the same. For example, if both the plain-texts begin with `the`, then they would be encrypted to the same value and when the cipher-texts are xor'd, there will be zeroes in the first three bytes. With this knowledge and knowing that the plaintext is likely to contain ASCII characters, we can systematically recover at least some of the plaintext.

In the case of encrypting multiple images with the same `pad`, we can deduce hidden patterns by xor-ing the encrypted images.

## Exploit

As explained above, the exploit involves xor-ing the given images with the hope that some pattern is revealed. So each byte of `image1.png` must be xor'd with the corresponding byte of `image2.png`. However, the file headers themselves should remain unchanged so that the resulting binary is still a `png` file.

For this purpose, we can use python's `PIL` library (install using `pip3 install pillow`). The code is simple and is as follows:

```python
from PIL import Image, ImageChops

# Open images
im1 = Image.open("image1.png")
im2 = Image.open("image2.png")

# xor byte-wise and save to file
result = ImageChops.logical_xor(im1,im2)
result.save('result.png')
```

Here is the `result.png`:

![result.png](result.png)

We have not obtained the flag yet since the format must adhere to `flag{...}`. The letters correspond to a `base64` encoding. So we can easily decode those using the following:

```python
from base64 import b64decode

encoded_flag = b"ZmxhZ3wbjNfdDFtM19QQGQhfQ=="
true_flag = b64decode(encoded_flag)
print(f'The flag is { true_flag }')
```

The output of the above code is:

```plaintext
The flag is b'flag{0n3_tim3_P@d!}'
```

## Flag

`flag{0n3_t1m3_P@d!}` 
