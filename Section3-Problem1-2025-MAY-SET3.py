
def overall_run_stats(batsman_data:list) -> dict:
    """Returns a dict with overall run statistics with keys 'min', 'max', 'total' and 'average'."""
    
    
    all_runs = [run for runs in batsman_data.values() for run in runs]
    total = sum(all_runs)
    return {
        'min':min(all_runs),
        'max': max(all_runs),
        'total': total,
        'average': round(total/ len(all_runs))
    }
    

def century_rate(runs:list) -> int:
    """Returns the century rate from the given runs.
    
    century_rate = n_centuries / n_matches * 100
    
    Century is assumed when the runs scored is greater than or equal to 100.

    Args:
        runs (list): Runs scored in different matches.

    Returns:
        int: Century Rate rounded to nearest integer.
    """
    
    
    return round(sum(1 for run in runs if run >=100)/len(runs)*100)
    

def average_yearly_century_rate(batsman_data:dict) -> int:
    """Average yearly century rate over all years."""
    
    
    return round(
        sum(century_rate(runs) for runs in batsman_data.values())
        /len(batsman_data)
    )
    

def years_with_more_than_average_yearly_century_rate(batsman_data:dict) -> set:
    """Returns a set of years with century rate more than the average yearly century rate."""
    
    
    avg_cen_rate = average_yearly_century_rate(batsman_data)
    return {year for year in batsman_data if century_rate(batsman_data[year])>avg_cen_rate}
    

def year_with_most_average_runs(batsman_data:dict) -> int:
    """Returns the year with the most average runs."""
    
    
    avg = lambda x: sum(x)/len(x)
    return max(batsman_data, key= lambda x: (avg(batsman_data.get(x)),-x))
    
# #Another Method

#   def overall_run_stats(batsman_data:list) -> dict:
#     """Returns a dict with overall run statistics with keys 'min', 'max', 'total' and 'average'."""
#     d={}
#     for i in batsman_data.values():
#         if "total" not in d.keys():
#             d["total"]=sum(i)
#             d["min"]=min(i)
#             d["max"]=max(i)
#             d["average"]=len(i)
#         else:
#             d["total"] +=sum(i)
#             d["min"]= min(i) if min(i)<d["min"] else d["min"]
#             d["max"]= max(i) if max(i)>d["max"] else d["max"]
#             d["average"] +=len(i)
            
#     d["average"]=round(d["total"]/d["average"])
#     return d
        
        
    

# def century_rate(runs:list) -> int:
#     """Returns the century rate from the given runs.
    
#     century_rate = n_centuries / n_matches * 100
    
#     Century is assumed when the runs scored is greater than or equal to 100.

#     Args:
#         runs (list): Runs scored in different matches.

#     Returns:
#         int: Century Rate rounded to nearest integer.
#     """
#     c=0
#     l=len(runs)
#     for i in runs:
#         if i>=100:
#             c=c+1
    
#     return round(c/l * 100)
    

# def average_yearly_century_rate(batsman_data:dict) -> int:
#     """Average yearly century rate over all years."""
    
#     sum,c=0,0
#     for key,values in batsman_data.items():
#         sum=sum+century_rate(values) 
#         c=c+1
#     return round(sum/c)

# def years_with_more_than_average_yearly_century_rate(batsman_data:dict) -> set:
#     """Returns a set of years with century rate more than the average yearly century rate."""
#     avg=average_yearly_century_rate(batsman_data)
#     l=[]
#     sum,c=0,0
#     for key,values in batsman_data.items():
#         if century_rate(values) > avg:
#             l.append(key)
        
#     return set(l)
    
    
    

# def year_with_most_average_runs(batsman_data:dict) -> int:
#     """Returns the year with the most average runs."""
#     max=0 
#     sum1=0
#     c=0
#     output=0
    
#     for key,values in batsman_data.items():
#         sum1=sum(values)
#         c=len(values)
#         avg=sum1/c 
        
#         if avg>max:
#             max=avg
#             output = key
#         if avg==max:
#             if key <output:
#                 output = key
    
#     return output
        
        
#         Batsman Performance Analysis
# Given the runs scored in matches played by a batsman in his career as a dict with the year as key and the list of runs scored on matches in that year as values, write functions to do following analysis on the data.

# overall_run_stats(batsman_data: dict): return, min, max, total and average runs considering all matches over all years as a dictionary with keys "min", "max", "total" and 'average' respectively. Average is rounded as integer.
# century_rate(runs: list): Century rate is the number of centuries (greater than or equal to 100 runs) divided by number of matches played multiplied by 100 (rounded to nearest integer).
# average_yearly_century_rate(batsman_data: dict): average of the 'yearly century rate'.
# years_with_more_than_average_yearly_century_rate(batsman_data: dict): The year in which the batsman's yearly century rate is more than the "average yearly century rate".
# year_with_most_average_runs(batsman_data:dict): The year in which the batsman has scored most average runs scored. In case of ties return the earliest year.
# Examples

# >>> data = {
#     2016: [88, 66, 130, 122, 117, 95, 86],
#     2017: [149, 66, 110],
#     2018: [157, 84],
#     2019: [148, 127, 71, 117],
#     2020: [91, 156, 80, 135, 152, 109]
# }
# >>> overal_base_stats(data)
# {'average': 112, 'max': 157, 'min': 66, 'total': 2456}
# >>> century_rate(data[2016])
# 43
# >>> average_yearly_century_rate(data)
# 60
# >>> years_with_more_than_average_yearly_century_rate(data),
# {2017, 2019, 2020}
# >>> year_with_most_average_runs(data),
# 2018


#
