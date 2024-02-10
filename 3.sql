SELECT OrderID, SUM(UnitPrice * Quantity) AS total
FROM Order_Details
GROUP BY OrderID
HAVING SUM(UnitPrce * Quantity) > 10000