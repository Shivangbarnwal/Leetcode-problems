class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        min_finish_time = float('inf')
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Land first
                land_start = landStartTime[i]
                land_end = land_start + landDuration[i]
                water_start_after_land = max(land_end, waterStartTime[j])
                finish1 = water_start_after_land + waterDuration[j]
    
                # Water first
                water_start = waterStartTime[j]
                water_end = water_start + waterDuration[j]
                land_start_after_water = max(water_end, landStartTime[i])
                finish2 = land_start_after_water + landDuration[i]
    
                # Update minimum finish time
                min_finish_time = min(min_finish_time, finish1, finish2)
        
        return min_finish_time