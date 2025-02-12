# Syllabus

>C. Source Code. Machine Code. Compiler. Correctness, Design, Style. Visual Studio Code. Syntax Highlighting. Escape Sequences. Header Files. Libraries. Manual Pages. Types. Conditionals. Variables. Loops. Linux. Graphical User Interface (GUI). Command-Line Interface (CLI). Constants. Comments. Pseudocode. Operators. Integer Overflow. Floating-Point Imprecision.


# Notes

## Machine Code

``` C
#include<stdio.h> //standard io.h

int main(void) //void -no input
{
	printf("hello world\n")
}
```


The computer can onlrecy ognize the binary numbers so we need a compiler(编译器) to make the higher level language to a lower level language.

![[compiler.svg]]

use a cloud(best) [URL](https://cs50.dev) or you can use VS code in your computer

Some words you should know: GUI CLI


## Hello world

``` C
#include<stdio.h>
//pronounced "include standard io.h"

int main(void)
{
	printf("hello world\n")
}
```


Some little concepts:

`#include stdio.h` - include standard io.h
`curly braces` - 大括号{}
`printf` - F means formatted
`semicolon` - 分号;
`syntax` - 句法

In the terminal

``` 
$ code hello.c
$ make hello
// not need to input hello.c make can look the folder
// make to compile the file from source code to machine code
$ ./hello

and get the 
hello world$(\n)
```


## Library(Header Files) 

We can use the code others write before via library and for example we can find the stdio.h 
[Manual Pages](https:/manual.cs50.io/#stdio.h) 

``` C
printf("hello, %s\n", answer)
// %s means a place holder
```


Case 1
``` C
#include <stdio.h>

int main(void)
{
	string answer = get_string("What's your name?");
	printf("hello, &s\n", answer);
}
```

**Error:** get_string is not claimed.

Case 2
``` C
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	string answer = get_string("What's your name?");
	printf("hello, &s\n", answer);
}
```

Here gets so many cases and we can design the programs so that it can be more efficient.

## Terminal Commands

*We can know more about them by Google.*

In the terminal window, some common command-line arguments we may use include:

- `cd`, for changing our current directory (folder)
- `cp`, for copying files and directories
- `ls`, for listing files in a directory
- `mkdir`, for making a directory
- `mv`, for moving (renaming) files and directories
- `rm`, for removing (deleting) files
- `rmdir`, for removing (deleting) directories


## Types of the variablews

Types with which you might interact during this course include:

- `bool`, a Boolean expression of either true or false
- `char`, a single character like a or 2
- `double`, a floating-point value with more digits than a float
- `float`, a floating-point value, or a real number with a decimal value
- `int`, integers up to a certain size, or number of bits
- `long`, integers with more bits, so they can count higher than an int
- `string`, a string of characters

Followings are make the Scratch codes to C. 

## Conditionals

Some tips:
	Don't make some unnecessary operations.
	Focus on how to design the better structure of codes.

``` C
if (x < y)
{
    printf("x is less than y\n");
}
else if (x > y)
{
    printf("x is greater than y\n");
}
else
{
    printf("x is equal to y\n");
}
```


But not make the three ifs because it will waste the time.

## Loop

Motivation: We want to let the vsc meows like the Scratch and how should we do?
Answer: We can make a loop to decrease our codes.

``` C
#include <cs50.h>
#include <stdio.h>

void meow(int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number: ");
    }
    while (n < 1);
    meow(n);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

>Comments
>Typically, each comment is a few words or more, providing the reader an opportunity to understand what is happening in a specific block of code. Further, such comments serve as a reminder for you later when you need to revise your code.

## Functions 

An inspiring idea is to make the repeating parts a new role that we can use them by include or write the function's name.

Here's a example from Mario(循环嵌套).
Notice how printing a row is accomplished through a new function.

``` C
// Helper function

#include <stdio.h>

void print_row(int width);

//void means no output , int width means we have one input
  
int main(void)
{
    const int n = 3;
    for (int i = 0; i < n; i++)
    {
        print_row(n);
    }
}

//Row function
void print_row(int width)
{
    for (int i = 0; i < width; i++)
    {
        printf("#");
    }
    printf("\n");
}
```

## Calculator

``` C
// int

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int dollars = 1;
    while (true)
    {
        char c = get_char("Here's $%i. Double it and give to next person? ", dollars);
        if (c == 'y')
        {
            dollars *= 2;
        }
        else
        {
            break;
        }
    }
    printf("Here's $%i.\n", dollars);
}
```

- Types are very important because each type has specific limits. For example, because of the limits in memory, the highest value of an `int` can be `4294967295`. If you attempt to count an `int` higher, an _integer overflow_ will result where an incorrect value will be stored in this variable.
- The number of bits limits how high and low we can count.
- This can have catastrophic, real-world impacts.
- We can correct this by using a data type called `long`.


``` C
// long

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long dollars = 1;
    while (true)
    {
        char c = get_char("Here's $%li. Double it and give to next person? ", dollars);
        if (c == 'y')
        {
            dollars *= 2;
        }
        else
        {
            break;
        }
    }
    printf("Here's $%li.\n", dollars);
}
```


## Truncation

``` C
// Division with ints, demonstrating truncation

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("x: ");

    // Prompt user for y
    int y = get_int("y: ");

    // Divide x by y
    printf("%i\n", x / y);
}
```

An integer divided by an integer will **always result in an integer** in C. Accordingly, the above code will often result in any digits after the decimal being thrown away.

``` C
// Floats

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    float x = get_float("x: ");

    // Prompt user for y
    float y = get_float("y: ");

    // Divide x by y
    printf("%.50f\n", x / y);
}
```

- _Floating point imprecision_ illustrates that there are limits to how precise computers can calculate numbers.
- As you are coding, pay special attention to the types of variables you are using to avoid problems within your code.
- We examined some examples of disasters that can occur through type-related errors.

# Sum up

- How to create your first program in C.
- How to use the **command line**.
- About predefined **functions** that come natively with C.
- How to use variables, **conditionals**, and **loops**.
- How to create your own functions to simplify and improve your code.
- How to er codevaluate you on three axes: correctness, design, and style.
- How to integrate comments into your code.
- How to utilize types and operators and the implications of your choices.


# Problem Set 1

## What to Do

1. Log into [submit.cs50.io](https://submit.cs50.io/) using your GitHub account and click **Authorize cs50**, then close the tab.
2. Log into [cs50.dev](https://cs50.dev/) using your GitHub account to access your very own “codespace.”
3. Once your codespace has loaded, close any **Welcome** tabs that might have opened by default.
4. Run `update50` in your codespace’s terminal window to ensure that your codespace is up-to-date and, if prompted, click **Rebuild now**.
5. Complete [Hello, World](https://cs50.harvard.edu/x/2025/psets/1/world/).
6. Submit [Hello, It’s Me](https://cs50.harvard.edu/x/2025/psets/1/me/).
7. Submit one of:
    - [this version of Mario](https://cs50.harvard.edu/x/2025/psets/1/mario/less/), if feeling less comfortable
    - [this version of Mario](https://cs50.harvard.edu/x/2025/psets/1/mario/more/), if feeling more comfortable
8. Submit one of:
    - [Cash](https://cs50.harvard.edu/x/2025/psets/1/cash/), if feeling less comfortable
    - [Credit](https://cs50.harvard.edu/x/2025/psets/1/credit/), if feeling more comfortable

If you submit both versions of Mario, we’ll record the higher of your two scores. If you submit both Cash and Credit, we’ll record the higher of your two scores.

## Advice

- Try out any of David’s programs from class via [Week 1](https://cs50.harvard.edu/x/2025/weeks/1/)’s source code.
- See CS50’s [style guide for C](https://cs50.readthedocs.io/style/c/) for tips on how to improve your code’s style.
- If you see any errors when compiling your code with `make`, focus first on fixing the very first error you see, scrolling up as needed.
- If unsure what it means, try asking `help50` for help. For instance, if trying to compile `hello`, and `make hello` is yielding errors, try running `help50 make hello` instead!

## My Submit

### Hello

``` C
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name?");
    printf("hello, %s\n",name);
}
```



### Mario-more

``` C
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height= ");
    }
    while (height < 1 || height > 8);
    int row = 0;
    while (row < height)
    {
        for (int i = 0; i < height - row - 1; i++)
        {
            printf(" ");
        }
        for (int j = 0; j < row + 1; j++)
        {
            printf("#");
        }
        printf("  ");
        for (int j = 0; j < row + 1; j++)
        {
            printf("#");
        }
        row++;
        printf("\n");
    }
}
```



### Cash

> Greedy Algorithms
> Fortunately, computer science has given cashiers everywhere ways to minimize numbers of coins due: greedy algorithms.
> According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one “that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems.”
> What’s all that mean? Well, suppose that a cashier owes a customer some change and in that cashier’s drawer are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). The problem to be solved is to decide which coins and how many of each to hand to the customer. Think of a “greedy” cashier as one who wants to take the biggest bite out of this problem as possible with each coin they take out of the drawer. For instance, if some customer is owed 41¢, the biggest first (i.e., best immediate, or local) bite that can be taken is 25¢. (That bite is “best” inasmuch as it gets us closer to 0¢ faster than any other coin would.) Note that a bite of this size would whittle what was a 41¢ problem down to a 16¢ problem, since 41 - 25 = 16. That is, the remainder is a similar but smaller problem. Needless to say, another 25¢ bite would be too big (assuming the cashier prefers not to lose money), and so our greedy cashier would move on to a bite of size 10¢, leaving him or her with a 6¢ problem. At that point, greed calls for one 5¢ bite followed by one 1¢ bite, at which point the problem is solved. The customer receives one quarter, one dime, one nickel, and one penny: four coins in total.
> It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally so for America’s currency (and also the European Union’s). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible. How few? Well, you tell us!



``` C
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int changeOwed;
    do
    {
        changeOwed = get_int("Change owed: ");
    }
    while (changeOwed < 0);

    int quarters;
    int dimes;
    int nickels;
    int pennies;

    quarters = changeOwed / 25;
    changeOwed = changeOwed - quarters * 25;
    dimes = changeOwed / 10;
    changeOwed = changeOwed - dimes * 10;
    nickels = changeOwed / 5;
    changeOwed = changeOwed - nickels * 5;
    pennies = changeOwed;

    int k = quarters + dimes + nickels + pennies;
    printf("%i\n", k);

}
``` 


### Credit

> Luhn’s Algorithm
> So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:
> 1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
> 2. Add the sum to the sum of the digits that weren’t multiplied by 2.
> 3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
> That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014.
> 1. For the sake of discussion, let’s first underline every other digit, starting with the number’s second-to-last digit:
>     4003600000000014
>     Okay, let’s multiply each of the underlined digits by 2:
>     1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2
>     That gives us:
>     2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
>     Now let’s add those products’ digits (i.e., not the products themselves) together:
>     2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
> 2. Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):
>     13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
> 3. Yup, the last digit in that sum (20) is a 0, so David’s card is legit!
> So, validating credit card numbers isn’t hard, but it does get a bit tedious by hand. Let’s write a program.



``` C
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long checknum;
    // get a number
    checknum = get_long("Number: ");
    // 最终求和变量
    int checksum = 0;
    // 指示变量
    int digit = 1;
    
    // checksum part
    int reminder;
    int save1 = 0;
    int save2 = 0;
    while (checknum > 0)
    {
        save2 = save1;
        save1 = 0;
        reminder = 0;
        if (digit % 2 == 0)
        {
            save1 = checknum % 10;
            reminder = checknum % 10 * 2;
            checknum /= 10;
            if (reminder >= 10)
            {
                reminder = reminder % 10 + 1;
                checksum += reminder;
            }
            else
            {
                checksum += reminder;
            }
        }
        else
        {
            save1 = checknum % 10;
            checksum += checknum % 10;
            checknum /= 10;
        }
        digit += 1;
    }
    digit -= 1;
    
    // claim
    if (checksum % 10 == 0)
    {
        if (save1 == 3 && digit == 15)
        {
            if (save2 ==4 || save2 == 7)
            {
                 printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (save1 == 5 && digit == 16)
        {
            if (save2 >=1 && save2 <= 5)
            {
                 printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (save1 == 4 && (digit ==13 || digit == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
```



