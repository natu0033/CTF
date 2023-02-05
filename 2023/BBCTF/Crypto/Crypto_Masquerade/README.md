# [Crypto] Crypto_Masquerade

# 問題文
The truth is hidden in the shadows, masked by a facade of deception. Peel back the layers and look deeper to reveal the truth.

# 問題内容
確認中。

flag{wA17_1tS_all_rs4?_Alw4ys_H4S_b33N}

```python
# coding:utf-8

# import
import base64

from Crypto.Util import number
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

BIT_L = 2**8

# fanc
def generate_secrets(pg, g):
    p = pg // g
    g = g
    h = (p - 1) * (g - 1)
    a = 0
    while number.GCD(a, h) != 1:
        a = number.getRandomRange(3, h)
    b = pow(a, -1, h)
    return p * g, g, a, b

# main
if __name__ == '__main__':
    oP = 6370378468881927509755384118503111539874702347049417136057766685502676572863635325176179080343015344300474835093751507585475975880958399175729652358997441
    oG = 89492589226316046023047445790085729135714145446293330308765949876011038911289
    message = 'gAAAAABj3sNu6bTn4rpsj_AsyHS_hu18K5jxkT9gsl9SMjjEkQ7sIn5CbkDMwHVibbAXMF9ei-Z3PvmmejFduBg9QwLUJ5zO1U_2Muar6OUoPznqN9A-_u6HNq_ZyLsaPJsxQWdGXWgT'

    p, g, a, b = generate_secrets(oP, oG)

    A = pow(g, a, p)
    B = pow(g, b, p)
    key = pow(A, b, p)

    password = key.to_bytes((key.bit_length() + 7) // 8, "big")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=b"\x00" * 8,
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    token = message.encode('ascii')
    flag = f.decrypt(token).decode()

    print(flag)
    
```
