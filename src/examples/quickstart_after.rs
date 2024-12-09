/// Returns a vector containing the first n Fibonacci numbers.
pub fn fibonacci(n: u64) -> Vec<u64> {
    if n == 0 {
        return vec![];
    }

    let mut fib = Vec::with_capacity(n as usize);
    fib.push(0);

    if n == 1 {
        return fib;
    }

    fib.push(1);

    for _ in 2..n {
        let next = fib[fib.len() - 1] + fib[fib.len() - 2];
        fib.push(next);
    }

    fib
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
