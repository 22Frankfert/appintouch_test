SELECT Territorries.TerritoryDescription, Region.RegionDescribtion
FROM Territorries
JOIN Region ON Territorries.RegionID = Region.RegionID