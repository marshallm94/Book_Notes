# Computer Systems: A Programmers Perspective

[TOC]

## Unorganized Thoughts

## Chapter Insights

### 1

### 2 - Representing and Manipulating Information

**Bits, Bytes, & Data Types**

* Different data types use a different number of bytes to store information.
    * The number of bytes used to store information determines the bounds of information available to be stored

From the [MySQL Documentation](https://dev.mysql.com/doc/refman/8.0/en/integer-types.html):

```
| Type      | Storage (Bytes) | Minimum Value Signed | Minimum Value Unsigned | Maximum Value Signed | Maximum Value Unsigned |
| --------- | --------------- | -------------------- | ---------------------- | -------------------- | ---------------------- |
| TINYINT   | 1               | -128                 | 0                      | 127                  | 255                    |
| SMALLINT  | 2               | -32768               | 0                      | 32767                | 65535                  |
| MEDIUMINT | 3               | -8388608             | 0                      | 8388607              | 16777215               |
| INT       | 4               | -2147483648          | 0                      | 2147483647           | 4294967295             |
| BIGINT    | 8               | -2^( 63 )            | 0                      | 2^( 63 )-1           | 2^( 64 )-1             |
```

I'm going to "pivot" this table to make things a little easier to work with...

```
| Type      | Storage (Bytes) | Signed or Unsigned | Minimum Value | Maximum Value |
| --------- | --------------- | ------------------ | ------------- | ------------- |
| TINYINT   | 1               | Signed             | -128          | 127           |
| TINYINT   | 1               | Unsigned           | 0             | 255           |
| SMALLINT  | 2               | Signed             | -32768        | 32767         |
| SMALLINT  | 2               | Unsigned           | 0             | 65535         |
| MEDIUMINT | 3               | Signed             | -8388608      | 8388607       |
| MEDIUMINT | 3               | Unsigned           | 0             | 16777215      |
| INT       | 4               | Signed             | -2147483648   | 2147483647    |
| INT       | 4               | Unsigned           | 0             | 4294967295    |
| BIGINT    | 8               | Signed             | -2^( 63 )     | 2^( 63 )-1    |
| BIGINT    | 8               | Unsigned           | 0             | 2^( 64 )-1    |
```

Lets define where these minimum and maximum values come from:
* There are 8 bits in a byte. So the above table could be have an additional column "Storage (Bits)":

```
| Type      | Storage (Bytes) | Storage (Bits)                      | Signed or Unsigned | Minimum Value | Maximum Value |
| --------- | --------------- | ----------------------------------- | ------------------ | ------------- | ------------- |
| TINYINT   | 1               | (Storage (Bytes) * 8) == 1 * 8 = 8  | Signed             | -128          | 127           |
| TINYINT   | 1               | (Storage (Bytes) * 8) == 1 * 8 = 8  | Unsigned           | 0             | 255           |
| SMALLINT  | 2               | (Storage (Bytes) * 8) == 2 * 8 = 16 | Signed             | -32768        | 32767         |
| SMALLINT  | 2               | (Storage (Bytes) * 8) == 2 * 8 = 16 | Unsigned           | 0             | 65535         |
| MEDIUMINT | 3               | (Storage (Bytes) * 8) == 3 * 8 = 24 | Signed             | -8388608      | 8388607       |
| MEDIUMINT | 3               | (Storage (Bytes) * 8) == 3 * 8 = 24 | Unsigned           | 0             | 16777215      |
| INT       | 4               | (Storage (Bytes) * 8) == 4 * 8 = 32 | Signed             | -2147483648   | 2147483647    |
| INT       | 4               | (Storage (Bytes) * 8) == 4 * 8 = 32 | Unsigned           | 0             | 4294967295    |
| BIGINT    | 8               | (Storage (Bytes) * 8) == 8 * 8 = 64 | Signed             | -2^( 63 )     | 2^( 63 )-1    |
| BIGINT    | 8               | (Storage (Bytes) * 8) == 8 * 8 = 64 | Unsigned           | 0             | 2^( 64 )-1    |
```

* A bit can have 2 states, notated with either a 0 or a 1. So, given N bits to work with, the question is:
    * **How many unique combinations of `0` and `1` are there in N bits?**
        * Answer: `2^N`
        * So lets add this as a column:

```
| Type      | Storage (Bytes) | Storage (Bits)                      | Number of Combinations Available                            |
| --------- | --------------- | ----------------------------------- | ----------------------------------------------------------- |
| TINYINT   | 1               | (Storage (Bytes) * 8) == 1 * 8 = 8  | (2 ^ Storage (Bits)) == 2 ^ 8  = 256                        |
| TINYINT   | 1               | (Storage (Bytes) * 8) == 1 * 8 = 8  | (2 ^ Storage (Bits)) == 2 ^ 8  = 256                        |
| SMALLINT  | 2               | (Storage (Bytes) * 8) == 2 * 8 = 16 | (2 ^ Storage (Bits)) == 2 ^ 16 = 65,536                     |
| SMALLINT  | 2               | (Storage (Bytes) * 8) == 2 * 8 = 16 | (2 ^ Storage (Bits)) == 2 ^ 16 = 65,536                     |
| MEDIUMINT | 3               | (Storage (Bytes) * 8) == 3 * 8 = 24 | (2 ^ Storage (Bits)) == 2 ^ 24 = 16,777,216                 |
| MEDIUMINT | 3               | (Storage (Bytes) * 8) == 3 * 8 = 24 | (2 ^ Storage (Bits)) == 2 ^ 24 = 16,777,216                 |
| INT       | 4               | (Storage (Bytes) * 8) == 4 * 8 = 32 | (2 ^ Storage (Bits)) == 2 ^ 32 = 4,294,967,296              |
| INT       | 4               | (Storage (Bytes) * 8) == 4 * 8 = 32 | (2 ^ Storage (Bits)) == 2 ^ 32 = 4,294,967,296              |
| BIGINT    | 8               | (Storage (Bytes) * 8) == 8 * 8 = 64 | (2 ^ Storage (Bits)) == 2 ^ 64 = 18,446,744,073,709,551,616 |
| BIGINT    | 8               | (Storage (Bytes) * 8) == 8 * 8 = 64 | (2 ^ Storage (Bits)) == 2 ^ 64 = 18,446,744,073,709,551,616 |
```

Once this is defined, the reasoning for the minimum and maximum values becomes a little clearer:
* For unsigned values:
    * Take the Number of Combinations Available and subtract 1 (this "1" is for storing the value `0`) - this is the
      maximum value.
    * `0` is the minumum value
* For signed values:
    * Take the Number of Combinations Available, divide by 2, and make that number negative - this is the minumum value.
    * Take the Number of Combinations Available, divide by 2 *and subtract 1* (this "1" is for storing the value `0`) -
      this is the maximum value.

```
| Type      | Storage (Bytes) | Storage (Bits)                      | Number of Combinations Available                            | Minimum Value | Maximum Value |
| --------- | --------------- | ----------------------------------- | ----------------------------------------------------------- | ------------- | ------------- |
| TINYINT   | 1               | (Storage (Bytes) * 8) == 1 * 8 = 8  | (2 ^ Storage (Bits)) == 2 ^ 8  = 256                        | -128          | 127           |
| TINYINT   | 1               | (Storage (Bytes) * 8) == 1 * 8 = 8  | (2 ^ Storage (Bits)) == 2 ^ 8  = 256                        | 0             | 255           |
| SMALLINT  | 2               | (Storage (Bytes) * 8) == 2 * 8 = 16 | (2 ^ Storage (Bits)) == 2 ^ 16 = 65,536                     | -32768        | 32767         |
| SMALLINT  | 2               | (Storage (Bytes) * 8) == 2 * 8 = 16 | (2 ^ Storage (Bits)) == 2 ^ 16 = 65,536                     | 0             | 65535         |
| MEDIUMINT | 3               | (Storage (Bytes) * 8) == 3 * 8 = 24 | (2 ^ Storage (Bits)) == 2 ^ 24 = 16,777,216                 | -8388608      | 8388607       |
| MEDIUMINT | 3               | (Storage (Bytes) * 8) == 3 * 8 = 24 | (2 ^ Storage (Bits)) == 2 ^ 24 = 16,777,216                 | 0             | 16777215      |
| INT       | 4               | (Storage (Bytes) * 8) == 4 * 8 = 32 | (2 ^ Storage (Bits)) == 2 ^ 32 = 4,294,967,296              | -2147483648   | 2147483647    |
| INT       | 4               | (Storage (Bytes) * 8) == 4 * 8 = 32 | (2 ^ Storage (Bits)) == 2 ^ 32 = 4,294,967,296              | 0             | 4294967295    |
| BIGINT    | 8               | (Storage (Bytes) * 8) == 8 * 8 = 64 | (2 ^ Storage (Bits)) == 2 ^ 64 = 18,446,744,073,709,551,616 | -2^( 63 )     | 2^( 63 )-1    |
| BIGINT    | 8               | (Storage (Bytes) * 8) == 8 * 8 = 64 | (2 ^ Storage (Bits)) == 2 ^ 64 = 18,446,744,073,709,551,616 | 0             | 2^( 64 )-1    |
```

All of this logic can be seen a little more clearly with a short program:

```python
# program
bits_per_byte = 8
n_bytes_available = [1, 2, 3, 4, 8]
for i in n_bytes_available:
    bits_available = i * bits_per_byte
    unique_combinations_of_bits_available = 2**bits_available

    # subtracting 1 combination to save for the "0" value
    unsigned_max_value = ( unique_combinations_of_bits_available ) - 1
    unsigned_min_value = 0

    # subtracting 1 combination to save for the "0" value
    signed_max_value = ( ( unique_combinations_of_bits_available ) / 2 ) - 1
    signed_min_value = -( ( unique_combinations_of_bits_available ) / 2 )

    print(f"{i} byte(s) = ...")
    print(f'\t{bits_available} bits')
    print(f'\tUnique combinations of {bits_available} bits = {unique_combinations_of_bits_available:,}')
    print(f'\tSigned range using {unique_combinations_of_bits_available:,} unique combinations: [{int( signed_min_value ):,}, {int( signed_max_value ):,}]')
    print(f'\tUnsigned range using {unique_combinations_of_bits_available:,} unique combinations: [{unsigned_min_value:,}, {unsigned_max_value:,}]')

# output
1 byte(s) = ...
        8 bits
        Unique combinations of 8 bits = 256
        Signed range using 256 unique combinations: [-128, 127]
        Unsigned range using 256 unique combinations: [0, 255]
2 byte(s) = ...
        16 bits
        Unique combinations of 16 bits = 65,536
        Signed range using 65,536 unique combinations: [-32,768, 32,767]
        Unsigned range using 65,536 unique combinations: [0, 65,535]
3 byte(s) = ...
        24 bits
        Unique combinations of 24 bits = 16,777,216
        Signed range using 16,777,216 unique combinations: [-8,388,608, 8,388,607]
        Unsigned range using 16,777,216 unique combinations: [0, 16,777,215]
4 byte(s) = ...
        32 bits
        Unique combinations of 32 bits = 4,294,967,296
        Signed range using 4,294,967,296 unique combinations: [-2,147,483,648, 2,147,483,647]
        Unsigned range using 4,294,967,296 unique combinations: [0, 4,294,967,295]
8 byte(s) = ...
        64 bits
        Unique combinations of 64 bits = 18,446,744,073,709,551,616
        Signed range using 18,446,744,073,709,551,616 unique combinations: [-9,223,372,036,854,775,808, 9,223,372,036,854,775,808]
        Unsigned range using 18,446,744,073,709,551,616 unique combinations: [0, 18,446,744,073,709,551,615]
```

# TODO( 2023-03-22 ): Walkthrough "Two's Complement Encodings"  

### 3

### etc

## Reasoning Checks

