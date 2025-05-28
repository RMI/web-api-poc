-- Retrieve all organizations
SELECT * FROM poc.organizations;

-- Retrieve all scenarios
SELECT * FROM poc.scenarios;

-- Retrieve a specific scenario by name
SELECT * FROM poc.scenarios WHERE name = 'Test Scenario';

-- Retrieve all geographic coverage for a specific scenario
SELECT g.name
FROM poc.scenario_geographic_coverage sgc
JOIN poc.geographic_coverage g ON sgc.geographic_coverage_id = g.id
WHERE sgc.scenario_id = (SELECT id FROM poc.scenarios WHERE name = 'Test Scenario');

-- Retrieve all sector coverage for a specific scenario
SELECT sc.name
FROM poc.scenario_sector_coverage ssc
JOIN poc.sector_coverage sc ON ssc.sector_coverage_id = sc.id
WHERE ssc.scenario_id = (SELECT id FROM poc.scenarios WHERE name = 'Test Scenario');
