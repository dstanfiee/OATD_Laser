# README_LLM.md

This repository is designed for process engineers assisted by GitHub Copilot for code creation. This file serves as a comprehensive context window for the LLM to ensure that every piece of generated code adheres to best practices for clarity, maintainability, and thorough documentation. Our aim is to produce code that is not only functional but also easily understandable by both humans and large language models to maintain high quality software as the repository changes over time.
---
## 1. Overview and Objectives
- **Purpose:**
    Guide the LLM to generate code that:
    - Follows clear coding conventions
    - Includes extensive inline comments and comprehensive documentation
    - Is written in a simple, maintainable style suitable for process engineers

- **Primary Goals:**
    - **Clarity:** Use descriptive naming and maintain a simple code structure.
    - **Documentation:** Include detailed inline comments and header docstrings.
    - **Best Practices:** Follow industry coding standards and effective repository management practices. For example, refer to [GitHub Repository Management Best Practices](https://docs.github.com/en/repositories/creating-and-managing-repositories) and [GitHub Coding Best Practices](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account).

For further reading on coding best practices, consider these resources:
- [Code Complete](https://en.wikipedia.org/wiki/Code_Complete)
- [Clean Code](https://en.wikipedia.org/wiki/Clean_Code)

---
## 2. Guidelines for Code Creation
### A. Code Clarity and Readability
- **Descriptive Naming:**
    Use meaningful names for variables, functions, and classes to ensure clarity. (no specific naming convention is mandated here, but adopting a consistent practice across projects is encouraged.)

- **Simple Structure**
    Keep functions and modules small and focused. Break complex logic into smaller, manageable pieces.

- **Formatting**
    Maintain consistent indentation, spacing, and line lengths throughout the code.

### B. Extensive Documentation
- **File-Level Comments**
    At the top of every file, include a header that outlines:
    - The purpose of the file.
    - An overview of its contents.
    - Any prerequisites or dependencies.

- **Function and Method Comments (Docstrings):**
    Each function/method should begin with a docstring that details:
    - **Purpose:** What the function does.
    - **Parameters:** Their types and descriptions.
    - **Returns:** What is returned and its type.
    - **Exceptions:** Any errors or edge cases handled.
    - **Rationale:** Why the function is implemented in that particular way

    We will adhere to the following style guides for  docstrings in the different languages. 
    
- **Google Python Style Guide** This style specifies that
    - The first line is a short summary of the function's purpose.
    - There is a blank line after the summary.
    - The subsequent section includes detailed descriptions of arguments, return values, exceptions, and any additional notes.

    For more details, see the [Google Python Style Guide - Comments and Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

- **Google R Style Guide** This style specifies that
    - Use `#'` to start each line of the docstring.
    - The first line is a short summary of the function's purpose.
    - Include sections for parameters, return values, and examples.

    For more details, see the [Google's R Style Guide](https://google.github.io/styleguide/Rguide.html).

- **MATLAB Style Guide** This style specifies that
    - Use `%` to start each line of the docstring.
    - The first line is a short summary of the function's purpose.
    - Include sections for parameters, return values, and examples.

    For more details, see the [MathWorks MATLAB Style Guide](https://www.mathworks.com/help/matlab/matlab_prog/style-guidelines.html).

- **Inline Comments:**
    Insert inline comments to explain non-obvious or complex sections of code. These should:
    - Explain the rationale behind algorithmic or design choices.
    - Replace "magic numbers" with named constants and comment on their signficance.

- **Placeholder for Unit Tests:**
    The LLM should suggest placeholders where unit tests can be added for each function or module to encourage test-drive development.

- **Clarification Requests:**
    When instructions are ambiguous, the LLM should ask clarifying questions before generating code.

### C. Best Practices and Coding Conventions
- **Adherence to Standards:**
    Follow established best practices and guidelines for coding. (For example, refer to the [Github Coding Best PRactices](https://docs.github/setting-up-and-managing-your-github-user-account).)

- **Consistency**
    Maintain a uniform style across all generated code. Every file, function, and code block should adhere to these conventions.

- **Documentation Updates:**
    Ensure that when code is modified, corresponding comments and docstrings are updated to remain consistent with the current implementation.

### 3. Example Code Snippets

#### Python
Below is an example of a well-documented function in Python using Google style docstrings:

```python
def calculate_sum(a, b):
    """Calculates the sum of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.

    Raises:
        ValueError: If either a or b is not an integer.
    
    Notes:
        This function assumes both inputs are integers. If not, a ValueError is raised.
    """
    # Validate that both inputs are integers.
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    
    # Compute and return the sum.
    return a + b  # Return the computed sum.
```

#### R
Below is an example of a well-documented function in R using the Google style guide:

```R
#' Calculates the sum of two integers.
#'
#' @param a The first integer.
#' @param b The second integer.
#' @return The sum of a and b.
#' @examples
#' calculate_sum(1, 2)
#' @export
calculate_sum <- function(a, b) {
  # Validate that both inputs are numeric.
  if (!is.numeric(a) || !is.numeric(b)) {
    stop("Both inputs must be numeric.")
  }
  
  # Compute and return the sum.
  return(a + b)
}
```

#### MATLAB
Below is an example of a well-documented function in MATLAB using MathWorks style guidelines:

```matlab
function result = calculate_sum(a, b)
    % Calculates the sum of two integers.
    %
    % Args:
    %     a (int): The first integer.
    %     b (int): The second integer.
    %
    % Returns:
    %     int: The sum of a and b.
    %
    % Raises:
    %     error: If either a or b is not an integer.
    %
    % Notes:
    %     This function assumes both inputs are integers. If not, an error is raised.

    % Validate that both inputs are integers.
    if ~isinteger(a) || ~isinteger(b)
        error('Both inputs must be integers.');
    end
    
    % Compute and return the sum.
    result = a + b;  % Return the computed sum.
end