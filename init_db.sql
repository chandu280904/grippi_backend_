-- init_db.sql
DROP TABLE IF EXISTS campaigns;

CREATE TABLE campaigns (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  status TEXT NOT NULL, -- 'Active' or 'Paused'
  clicks INTEGER NOT NULL,
  cost REAL NOT NULL,
  impressions INTEGER NOT NULL
);

INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES
('Summer Sale','Active',150,45.99,1000),
('Black Friday','Paused',320,89.50,2500),
('Back to School','Active',210,65.00,1800),
('Holiday Promo','Active',95,30.25,900),
('Clearance Event','Paused',50,10.00,400),
('New Launch','Active',400,120.75,5000),
('Referral Boost','Paused',75,20.00,700),
('Flash Deal','Active',180,55.50,1200),
('Weekend Special','Paused',60,15.99,600),
('Brand Awareness','Active',1000,300.00,15000);
