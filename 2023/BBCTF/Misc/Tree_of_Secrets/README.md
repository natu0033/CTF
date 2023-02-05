# [Misc] Tree_of_Secrets
### 問題文
The message is encoded in the whispers of the wind, buried deep in the roots of a tree. Uncover the secret by listening to the silence between the lines and exploring the branches.

### 問題内容
root.zipとmessageファイルが渡されてフラグを探す問題。

メッセージからrootのファイルパスをたどっていくと文字が拾えるのですべて変換する。
```
RkxBR3t3SGFUXzdIRV9IdUZmX000TiF9
```
結果をbase64で変換したらフラグがでた。
```
b'FLAG{wHaT_7HE_HuFf_M4N!}'
```

flag{wHaT_7HE_HuFf_M4N!}

-----
message
```
00011000110011110000000100110000101011001111100000111101011010101101000010111100110100101001101001010001101111111111111111010111010001001
```

root.zip
```bash
./root
├── 0
│   ├── 0
│   │   ├── 0
│   │   │   └── R
│   │   └── 1
│   │       ├── 0
│   │       │   └── 3
│   │       └── 1
│   │           └── U
│   └── 1
│       ├── 0
│       │   ├── 0
│       │   │   ├── 0
│       │   │   │   └── m
│       │   │   └── 1
│       │   │       └── Z
│       │   └── 1
│       │       └── d
│       └── 1
│           ├── 0
│           │   ├── 0
│           │   │   └── t
│           │   └── 1
│           │       └── z
│           └── 1
│               ├── 0
│               │   └── i
│               └── 1
│                   └── G
└── 1
    ├── 0
    │   ├── 0
    │   │   ├── 0
    │   │   │   └── F
    │   │   └── 1
    │   │       └── 9
    │   └── 1
    │       ├── 0
    │       │   └── I
    │       └── 1
    │           ├── 0
    │           │   └── S
    │           └── 1
    │               └── V
    └── 1
        ├── 0
        │   ├── 0
        │   │   ├── 0
        │   │   │   └── k
        │   │   └── 1
        │   │       └── x
        │   └── 1
        │       └── X
        └── 1
            ├── 0
            │   ├── 0
            │   │   └── B
            │   └── 1
            │       └── T
            └── 1
                └── 0

40 directories, 21 files
```
