def summarize(nums: list) -> tuple:
    c = len(nums)
    nums_only = [n for n in nums if type(n) in (int, float)]
    cn = len(nums_only)
    ttl = sum(nums_only)
    avg = ttl / cn
    
    return c, cn, ttl, avg