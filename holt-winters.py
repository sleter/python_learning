#https://grisha.org/blog/2016/01/29/triple-exponential-smoothing-forecasting/ - simple example 

series = [3,10,12,13,12,10,12]

def average(series):
    """Veri naive approach"""
    return float(sum(series)/len(series))

def moving_average(series, n):
    """Average of last n points"""
    return average(series[-n:])

weights = [0.1, 0.2, 0.3, 0.4] # 10% + 20% + ... + 40% = 100% | weights that add up to more than 1 can give us bogus
def weighted_average(series, weights):
    """Values are given diferent weigths"""
    result = 0.0
    weights.reverse()
    for n in range(len(weights)):
        result += series[-n-1] * weights[n]
    return result

def exponential_smoothing(series, alpha): #each series has its best alpha (process of finding the best alpha i reffered to as fitting)
    """Given a series and alpha, return series of smoothed points"""
    result = [series[0]] # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])
    return result

def double_exponential_smoothing(series, alpha, beta):
    """With level and trend you can forecast TWO DATA POINTS ROTFLMAO"""
    result = [series[0]]
    for n in range(1, len(series)+1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series): # we are forecasting
          value = result[-1]
        else:
          value = series[n]
        last_level, level = level, alpha*value + (1-alpha)*(level+trend)
        trend = beta*(level-last_level) + (1-beta)*trend
        result.append(level+trend)
    return result

if __name__ == "__main__":
    pass