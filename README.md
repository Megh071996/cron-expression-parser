# cron-expression-parser

This python script parses a cron string and expands each field to show the times at which it will run in human readable format.

## Requirements

python>=3.11

# Usage

To run this program:
1. clone the repository to your local machine.

2. Open command prompt or terminal in root folder.

3. run:
```pip install -r requirements.py```

4. Install the package as binary:
```pip install --editable .```

5. Run the program with your cron expression.

Ex: 
```cron-expression-parser "*/15 0 1,15 * 1-5 /usr/bin/find"```

6. The output will be a table with human readable format:

```
    minute        0 15 30 45
    hour          0
    day of month  1 15
    month         1 2 3 4 5 6 7 8 9 10 11 12
    day of week   1 2 3 4 5
    command       /usr/bin/find
```

7. You can test the code as well:

    ```pytest```

