-- | Finds Length of a list
len :: [a] -> Int
len [x] = 1
len (x:xs) = 1 + len xs

-- | Gets sum of all numbers
sumL :: [Int] -> Int
sumL [x] = x
sumL (x:xs) = x + sumL xs

-- | Returns the sumation of numbers from 1 to x, where x is the parameter
sumN :: Int -> Int
sumN 1 = 1
sumN x = x + sumN (x-1)

-- | Ties it all together in O(n) time 
missingN :: [Int] -> Int
missingN x =  sumN (len x + 1) - sumL x 

main = do
print $ missingN [7,8,10,3,6,5,1,2,9]
