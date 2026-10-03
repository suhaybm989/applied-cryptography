from algorithms import extended_euclidean, generate_coefficients, repeated_squaring, sbox_substitution, apply_permutation, des_compute_L1_R1, XOR

gcd, x, y = extended_euclidean(240, 46)
assert gcd == 2 and 240 * x + 46 * y == gcd
for x, y in generate_coefficients(240, 46):
    assert 240 * x + 46 * y == gcd
assert repeated_squaring(5, 117, 113) == pow(5, 117, 113)
assert XOR('1100', '0101') == '1001'
substituted = sbox_substitution('0' * 48)
assert len(substituted) == 32
permuted = apply_permutation(substituted)
left, right = des_compute_L1_R1('0' * 32, '1' * 32, permuted)
assert left == '1' * 32 and right == permuted
print('Number theory and DES fragment examples passed.')
