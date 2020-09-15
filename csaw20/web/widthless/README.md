# CSAW 2020 Qualifiers : Widthless 
> **Category**: Web **Points**:50 **Description**:

Welcome to web! Let's start off with something kinda funky :)<br>
_http://web.chal.csaw.io:5018/_

### Solution:
Open the website and go through the source. First flag hint is in the comment
`<!-- zwsp is fun! -->`

`zwsp` stands for zero-width space steganography<br>
**Tool Used**: _https://github.com/enodari/zwsp-steg-py_<br>

curl the whole website and run the tool on it
```bash
curl http://web.chal.csaw.io:5018/ -o site.html
python3 zwsp-steg.py site.html
```

You get a base64 encoded string, decode it and you should get
`alm0st_2_3z`

Submit that to the form in the homepage. The page returns a path
`/ahsdiufghawuflkaekdhjfaldshjfvbalerhjwfvblasdnjfbldf/<pwd>`

Navigate to: 
`http://web.chal.csaw.io:5018/ahsdiufghawuflkaekdhjfaldshjfvbalerhjwfvblasdnjfbldf/alm0st_2_3z`

More of zwsp, repeat the initial process and you should get a hex value:
`5f756e6831645f6d3`

Converting this to bytes produces:
`u_unh1d_m3`

Again, submit that to the form in the homepage. The page returns a path
`/19s2uirdjsxbh1iwudgxnjxcbwaiquew3gdi/<pwd1>/<pwd2>`

Navigate to:
`http://web.chal.csaw.io:5018/ahsdiufghawuflkaekdhjfaldshjfvbalerhjwfvblasdnjfbldf/alm0st_2_3z/u_unh1d_m3`

There's your flag !

### Flag
flag{gu3ss_u_f0und_m3}
