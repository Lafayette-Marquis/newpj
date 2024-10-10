
# Function to organize input by alphabetical or numerical order
organize_input <- function(input) {
  # Check if input is numeric
  if (all(suppressWarnings(!is.na(as.numeric(input))))) {
    # If numeric, convert to numeric and sort
    sorted_input <- sort(as.numeric(input))
  } else {
    # If not numeric, sort alphabetically
    sorted_input <- sort(input)
  }
  return(sorted_input)
}

# Example usage:
# Alphabetical sorting
words <- c("apple", "zebra", "banana", "cat")
print(organize_input(words))

# Numerical sorting
numbers <- c("10", "2", "1", "5")
print(organize_input(numbers))
