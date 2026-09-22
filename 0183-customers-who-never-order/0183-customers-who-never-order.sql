# Write your MySQL query statement below
select c.name as Customers from Customers as c Left join Orders as o on c.id = o.customerId
where customerId is null