use std::fs;
use std::cmp::max;
use std::ops::Range;

fn main() {

    fn bfs(grid: &mut Vec<Vec<char>>, i: usize, j: usize, fill: char) {
        let dirs: Vec<(i64, i64)> = vec![(1, 0), (-1,0), (0,1), (0, -1)];
        let mut queue: Vec<(usize, usize)> = Vec::new();
        queue.push((i,j));
        while let Some((cx, cy)) = queue.pop() {
            for &(dx, dy) in dirs.iter() {
                let nx = cx as i64 + dx;
                let ny = cy as i64 + dy;
                if nx < 0 || nx >= grid.len() as i64 || ny < 0 || ny >= grid[0].len() as i64 {
                    continue
                }
                let x: usize = nx as usize;
                let y: usize = ny as usize;

                if grid[x][y] == '.' {
                    grid[x][y] = fill;
                    queue.push((x,y));
                }
            }
        }
    }

    let contents = fs::read_to_string("src/bin/day9/data_ex.txt")
    .expect("Should have been able to read the file");

    let mut rows: usize = 0;
    let mut cols: usize = 0;
    // let mut largest_area: usize = 0;
    let mut points: Vec<Vec<usize>> = Vec::new();
    let mut grid: Vec<Vec<char>> = Vec::new();
    let mut largest_area: i64 = 0;
    for line in contents.lines() {
        let point = line.split(',').map(str::trim).map(str::parse::<usize>).collect::<Result<Vec<usize>,_>>().unwrap();
        points.push(vec![point[0], point[1]]);
    }
    for point in points.iter() {
        rows = max(rows, point[0]+2);
        cols = max(cols, point[1]+2);
    }
    for _ in 0..rows {
        let mut row_vec: Vec<char> = Vec::new();
        for _ in 0..cols {
            row_vec.push('.');
        }
        grid.push(row_vec);
    }
    let mut prev: Vec<usize> = points.last().unwrap().clone();
    for point in points.iter() {
        grid[point[0]][point[1]] = '#';
        if !prev.is_empty() {
            let start_end: Range<usize>;
            if prev[0] - point[0] == 0 {
                if prev[1] < point[1] {
                    start_end = prev[1]..point[1];
                } else {
                    start_end = point[1]..prev[1];
                }
                for i in start_end {
                    if !points.contains(&vec![point[0], i]) {
                        grid[point[0]][i] = 'X';
                    }
                }
            } else if prev[1] - point[1] == 0 {
                if prev[0] < point[0] {
                    start_end = prev[0]..point[0];
                } else {
                    start_end = point[0]..prev[0];
                }
                for i in start_end {
                    if !points.contains(&vec![i, point[1]]) {
                        grid[i][point[1]] = 'X';
                    }
                }
            }
        }
        prev = point.to_vec();
    }
    
    let mut xcoor: usize = 0;
    let mut ycoor: usize = 0;
    bfs(&mut grid, 0, 0, ':');
    for i in 0..rows {
        if grid[i].contains(&'.') { 
            xcoor = i;
            ycoor = grid[i].iter().position(| &x| x == '.').unwrap();
            break
        }
    }

    if xcoor != 0 && ycoor != 0 {
        bfs(&mut grid, xcoor, ycoor, 'X');
    }

    println!("fill done");

    
    for (i, point1) in points.iter().enumerate() {
        for (j, point2) in points.iter().enumerate() {
            if i <= j {
                continue
            }
            let x_start_end: Range<usize>;
            
            if point1[0] < point2[0] {
                x_start_end = point1[0]..point2[0];
            } else {
                x_start_end = point2[0]..point1[0];
            }
            
            
            let mut valid = true;
            for k in x_start_end {
                let y_start_end: Range<usize>;
                if point1[1] < point2[1] {
                    y_start_end = point1[1]..point2[1];
                } else {
                    y_start_end = point2[1]..point1[1];
                }
                for l in y_start_end {
                    if grid[k][l] == ':' {
                        valid = false;
                        break
                    }
                }
            }
            if valid {
                let area = ((point1[0] as i64 -point2[0] as i64 ).abs()+1)*((point1[1] as i64 -point2[1] as i64 ).abs()+1);
                largest_area = max(largest_area, area);
            }
        }
    }

    // for i in grid.iter() {
    //     println!("{:?}", i.iter().collect::<String>())
    // }
    println!("{}", largest_area)
}
