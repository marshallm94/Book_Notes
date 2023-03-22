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

* A bit can have 2 states, notated with either a 0 or a 1. So, given N bits to work with, **How many unique combinations
  of `0` and `1` are there in N bits?**
    * 2^N
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

Once this is defined, the reasoning for the minimum and maximum values becomes clear:
* For unsigned values:
    * Take the Number of Combinations Available and subtract 1 (this "1" is for storing the value `0`)
* For signed values

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


### 3

### etc

## Reasoning Checks

