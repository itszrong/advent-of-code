def main():
    with open("day2/data.txt", "r") as f:
        contents = f.read()

    res = 0
    for line in contents.splitlines():
      prev, prev_diff, valid = None, None, True
      for num in line.split():
        curr = int(num)
        if not prev:
          prev = curr
          continue
        diff = curr - prev
        if abs(diff) < 1 or abs(diff) > 3:
          valid = False
          break
        if prev_diff and ((prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0)):
          valid = False
          break
        prev_diff = diff
        prev = curr

      if valid:
        res += 1

    print(res)


if __name__ == "__main__":
    main()
