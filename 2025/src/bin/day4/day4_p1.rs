use std::fs;

fn main() {

    fn add(x: usize, y: i32) -> usize {
        if y.is_negative() {
            x - y.wrapping_abs() as u32 as usize
        } else {
            x + y as usize
        }
    }

    let contents = fs::read_to_string("src/bin/day4/data.txt")
        .expect("Should have been able to read the file");

    let grid: Vec<_> = contents.lines().map(|line| line.chars().collect::<Vec<_>>()).collect();
    let rows = grid.len();
    let cols = grid[0].len();
    let mut total = 0;
    for r in 0..rows {
        for c in 0..cols {
            if grid[r][c] == '@' {
                let dirs: Vec<(i32, i32)> = vec![(-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)];
                let mut neighbours = 0;
                for (dx, dy) in dirs {
                    if dx.is_negative() {
                        if r < dx.wrapping_abs() as u32 as usize {
                            continue
                        }
                    }
                    if dy.is_negative() {
                        if c < dy.wrapping_abs() as u32 as usize {
                            continue
                        }
                    }
                    let new_r = add(r, dx);
                    let new_c = add(c, dy);
                    if new_r < rows && new_c < cols {
                        if grid[new_r][new_c] == '@' {
                            neighbours += 1;
                        }
                    }

                }
                if neighbours < 4 {
                    total += 1;
                } 
            }
        }
    }
    println!("{:?}", grid);
    println!("{:?}", total);
}
