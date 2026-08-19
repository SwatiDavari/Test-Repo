pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_positive_numbers() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn it_adds_negative_and_positive() {
        assert_eq!(add(-1, 1), 0);
    }

    #[test]
    fn it_adds_zero() {
        assert_eq!(add(0, 0), 0);
    }

    #[test]
    fn it_is_commutative() {
        assert_eq!(add(4, 7), add(7, 4));
    }
}
