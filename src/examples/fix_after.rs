/// Returns a vector containing the first n numbers in the Fibonacci sequence.
pub fn fibonacci(n: u64) -> Vec<u64> {
    if n == 0 {
        return vec![];
    }
    let mut result = Vec::with_capacity(n as usize);
    result.push(0);
    if n == 1 {
        return result;
    }
    result.push(1);
    for _ in 2..n {
        let next = result[result.len() - 1] + result[result.len() - 2];
        result.push(next);
    }
    result
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
