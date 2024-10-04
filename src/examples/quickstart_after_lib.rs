/// Generates a vector containing the first `n` Fibonacci numbers.
pub fn fibonacci(n: u64) -> Vec<u64> {
    let mut sequence = Vec::with_capacity(n as usize);
    if n == 0 {
        return sequence;
    }
    sequence.push(0);
    if n == 1 {
        return sequence;
    }
    sequence.push(1);
    for _ in 2..n {
        let next = sequence[sequence.len() - 1] + sequence[sequence.len() - 2];
        sequence.push(next);
    }
    sequence
}

#[cfg(test)]
mod tests {}
