<h1 align="center">Text Readability Calculator</h1>

The "Text Readability Calculator" GitHub project is a tool designed to measure the readability of any English text. By leveraging the Coleman-Liau Index, this tool offers an efficient way to evaluate the difficulty level of written content, making it easier to ensure that the text is suitable for the intended audience.

<p align="center">
  <img src="https://github.com/Corentin-Lcs/text-readability-calculator/blob/main/DesMetrics.png" alt="DesMetrics.png"/>
</p>

## Coleman-Liau Readability Index

### Overview

The Coleman-Liau Index is a readability test designed to gauge the complexity of a text by analyzing its characters, words, and sentences. Unlike other readability tests, it does not rely on syllable counts but instead focuses on the number of characters, making it more suitable for digital text analysis.

The formula estimates the U.S. grade level needed to comprehend a given text, providing insights into the readability for different audiences.

### How It Works

The Coleman-Liau Index operates through the following steps:

1. **Character Count**:
   - The program counts the number of alphabetic characters in the text.

2. **Word Count**:
   - It calculates the number of words by identifying sequences of characters separated by spaces.

3. **Sentence Count**:
   - Sentences are detected by identifying punctuation marks that typically signal the end of a sentence (e.g., periods, exclamation marks, question marks).

4. **Computation**:
   - The formula is applied to compute the Coleman-Liau Index, giving a score that corresponds to a U.S. grade level.

### Reference Table

The Coleman-Liau Index is mapped to U.S. grade levels as follows:

| Index Score | Grade Level        | Age Range       | Notes                                                            |
|-------------|--------------------|-----------------|------------------------------------------------------------------|
| 0.0 - 0.9   | Kindergarten       | 5 - 6 years     | Extremely simple text. Suitable for very young children.         |
| 1.0 - 1.9   | 1st - 2nd Grade    | 6 - 8 years     | Very easy to read. Suitable for young children.                  |
| 2.0 - 2.9   | 3rd Grade          | 8 - 9 years     | Easy to read, appropriate for younger children.                  |
| 3.0 - 3.9   | 4th Grade          | 9 - 10 years    | Simple reading level, for children.                              |
| 4.0 - 4.9   | 5th Grade          | 10 - 11 years   | Text suitable for primary school students.                       |
| 5.0 - 5.9   | 6th Grade          | 11 - 12 years   | Understandable for late elementary students.                     |
| 6.0 - 6.9   | 7th Grade          | 12 - 13 years   | Common reading level for middle school students.                 |
| 7.0 - 7.9   | 8th Grade          | 13 - 14 years   | Simple reading for teenagers.                                    |
| 8.0 - 8.9   | 9th Grade          | 14 - 15 years   | Accessible text for young high school students.                  |
| 9.0 - 9.9   | 10th Grade         | 15 - 16 years   | Suitable for intermediate high school students.                  |
| 10.0 - 10.9 | 11th Grade         | 16 - 17 years   | Reading level appropriate for advanced teenagers.                |
| 11.0 - 11.9 | 12th Grade         | 17 - 18 years   | Text suited for high school seniors preparing for exams.         |
| 12.0 - 16.9 | College            | 18 - 22 years   | Suitable for college-level academic texts.                       |
| 17.0 +      | Professional       | 22 + years      | Complex, professional language often used in specialized fields. |

## Implementation Details

In this section, we break down the calculations integral to the Coleman-Liau Index, providing insight into how readability is quantitatively assessed.

### Formula

The Coleman-Liau Index is calculated using the following formula:

<p align="center">
  <img src="https://github.com/Corentin-Lcs/text-readability-calculator/blob/main/Formula A.png" alt="Formula A.png"/>
</p>

where:
- $`L`$ is the average number of characters per 100 words.
- $`S`$ is the average number of sentences per 100 words.

### Detailed Formula:

To compute $`L`$ and $`S`$:

```math
L = \left(\frac{n_{c}}{n_{w}}\right) \cdot 100
```   

```math
S = \left(\frac{n_{s}}{n_{w}}\right) \cdot 100
```

where:
- $`n_{c}`$ is the total number of alphabetic characters in the text.
- $`n_{s}`$ is the total number of sentences in the text.
- $`n_{w}`$ is the total number of words in the text.

Here is the expanded version of the formula:

<p align="center">
  <img src="https://github.com/Corentin-Lcs/text-readability-calculator/blob/main/Formula B.png" alt="Formula B.png"/>
</p>

## Usage

```
usage: desmetrics <input_file> [options]

DesMetrics - Calculate the Coleman-Liau Index of a text file.

positional arguments:
  input_file     path to the input .txt file

options:
  -h, --help     show this help message and exit
  -v, --verbose  enable verbose logging
  -V, --version  show program's version number and exit
```

## Project's Structure

```
text-readability-calculator/
├─ README.md
├─ LICENSE
├─ Formula A.png
├─ Formula B.png
├─ DesMetrics.png
└─ src/
   ├─ desmetrics.py
   └─ input_file.txt
```

## Meta

Created by [@Corentin-Lcs](https://github.com/Corentin-Lcs). Feel free to contact me!

Distributed under the GNU GPLv3 license. See [LICENSE](https://github.com/Corentin-Lcs/text-readability-calculator/blob/main/LICENSE) for more information.
