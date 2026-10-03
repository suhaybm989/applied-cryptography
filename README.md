# Applied cryptography

Selected Python functions extracted from my academic cryptography notebook, with neutral example inputs replacing personal data. This repository shows the code rather than the assessment report.

## Included

* Extended Euclidean algorithm and families of Bézout coefficients
* Modular exponentiation through repeated squaring
* DES permutation tables, S-box substitution, XOR and single-round operations
* A clean notebook and a Python module containing the same selected functions

## Run

Python 3.11 or later, with no third-party dependencies:

```sh
python examples.py
```

Expected output: `Number theory and DES fragment examples passed.`

The examples verify arithmetic identities and basic DES fragment behaviour. They are not cryptographic certification or full cipher test vectors.

## Scope and provenance

The algorithms are selected from my original coursework. The packaging and validation examples were prepared for this public code showcase. Assessment prose, student-derived inputs, contact details, saved outputs and original notebook metadata are excluded. New notebook outputs may be generated when you run it locally.

These are educational implementations. The DES pieces do not form a complete encryption library and DES is unsuitable for protecting modern data. AES and public-key exercises from the broader coursework are not represented in this selected code release. Use maintained cryptographic libraries for real applications.
