def largest_rectangle_area(heights):
    heights.append(0)
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area


heights = list(map(int, input().split()))[1:]

result = largest_rectangle_area(heights)
print(result)
