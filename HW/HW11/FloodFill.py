class FloodFill:
    def floodFill(self, image, sr, sc, newColor):
        originalColor = image[sr][sc]
        
        if originalColor == newColor:
            return image
        
        m, n = len(image), len(image[0])
        
        def dfs(x, y):
            if x<0 or x>=m or y<0 or y>=n or image[x][y]!=originalColor:
                return

            image[x][y] = newColor

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        dfs(sr, sc)
        
        return image