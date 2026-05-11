# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> All of the functions are considered hash functions because ther take an input key and convert it into 
> a numeric value that can be used to calculate an index in a hash map.
> They are designed to work efficiently so data can be stored and retrieved faster.
> Another property is that they can produce collisions, where different keys may generate the same
> has value

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> 1. This first one "the simplest hash function" is very fast and simple to implement as its name explain, but it is very poor uniformity because every key
> returns the same value. It also causes maximum collisions and I reckon it is not useful for real hash maps.
> 2. To understand properly this one I have to explain what ASCII actually mean. It's a character encoding standard that assigns a unique number
> (from 0 to 127) to every letter, digit, punctuation mark, and control character used in English. Computers only understand numbers
> (binary 0s and 1s) so ASCII is teh lookup table that tells computers when I type the letter 'B', store the number 65.
> Knowing that this kind of function is very easy to understand and implement, It works for variable length keys but different inputs
> can easily create the same result ("AB" and "BA") it has also poor collision resistance and poor distribution.
> 3. Let's talk about Pearson hashing. It is extremely simple, fast and works well for small keys (like strings or short messages)
> it is also sensitive to input changes.
> 4. Function that uses the built-in. The main advantages. Very fast and optimised for python and also good distribution for general programming use.
> on the other hand it is less predictable for testing purposes
> 5. The hash function who uses the SHA256 from the hashlib module is very strong collision resistance, excellent security and 
>  sensitivity to input changes that is why is used for authenticating software packages but as a disadvantage I can say that it 
> much slower than other functions

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> #### Efficiency: 
> A hash map should be fast when storing and retrieving data. If the hash function is too slow, 
> the advantages of the hash map are reduced.
> #### Determinism: 
> The same key must always generate the same hash value. Otherwise, it would not be possible 
> to reliably retrieve stored data.
> #### Uniformity: 
> Probably the most important because it spreads data evenly across the hash map. This reduces 
> collisions and improves performance.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> For this task, I would choose the sum of ASCII values hash function. It is simple, efficient, and easy 
> to understand for educational purposes. It also matches the requirements of the assessment because it is deterministic 
> and fast to compute. Even though it is not the strongest function for collision resistance, collisions can still be 
> handled correctly using PlayerLists as chaining structures in the hash map.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> The line random.seed(42) ensures the lookup table is always shuffled in the same way, which makes the hash function deterministic.

> The pearson_table creates a shuffled table of values from 0 to 255. This table works like a lookup system that helps spread hash values more evenly across the hash map.

> The variable hash_ = 0 initializes the starting hash value.

> The loop for char in key: processes the key one character at a time.

> The expression ord(char) converts each character into its ASCII numeric value.

> The XOR operation hash_ ^ ord(char) mixes the current hash value with the current character. This improves sensitivity to input changes because even small differences in the input can significantly change the final result.

> The line pearson_table[...] uses the mixed value to look up a new value from the shuffled table, helping create a more uniform distribution and reducing collisions.

> Finally, return hash_ % size ensures the result fits within the available indexes of the hash map.

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> I would do it in the following order

> 1. Receive the player's key and name.
> 2. Calculate the hash value using the key.
> 3. Use modulo (%) with the hash map size to get the index.
> 4. Access the PlayerList stored at that index.
> 5. Check whether the player already exists in that PlayerList.
> 6. If the player exists, update the player's information.
> 7. If the player does not exist:
   > - Create a new Player object.
   > - Insert the player into the PlayerList.
> 8. Increase the total player count.

## Reflection

1. What was the most challenging aspect of this task?

> The most challenging aspect was understanding how collisions work in a hash map and how to solve them using PlayerLists. 
> At first, it was confusing to understand why multiple players could end up in the same bucket. After testing collisions 
> and visualising the linked lists inside each bucket, I understood how chaining allows the hash map to still work correctly 
> even when collisions happen.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> If I did not have to use a PlayerList, I would probably use Python dictionaries internally because they are already highly optimized hash maps. 
> Another option would be using simple Python lists in each bucket because they are easier to implement and work with. 
> However, the PlayerList helped me better understand how collisions are handled manually and how linked data structures work together 
> with hash maps.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
