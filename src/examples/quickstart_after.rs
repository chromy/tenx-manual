/// Returns a vector containing the first n numbers in the Fibonacci sequence
pub fn fibonacci(n: u64) -> Vec<u64> {
    if n == 0 {
        return vec![];
    }
    if n == 1 {
        return vec![0];
    }

    let mut sequence = vec![0, 1];
    while sequence.len() < n as usize {
        let next = sequence[sequence.len() - 1] + sequence[sequence.len() - 2];
        sequence.push(next);
    }
    sequence
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fibonacci() {
        assert_eq!(fibonacci(0), vec![]);
        assert_eq!(fibonacci(1), vec![0]);
        assert_eq!(fibonacci(2), vec![0, 1]);
        assert_eq!(fibonacci(5), vec![0, 1, 1, 2, 3]);
        assert_eq!(fibonacci(8), vec![0, 1, 1, 2, 3, 5, 8, 13]);
    }
}
