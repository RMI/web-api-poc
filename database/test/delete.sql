-- Delete a scenario and ensure cascading deletes
DELETE FROM poc.scenarios
WHERE name = 'Test Scenario';

-- Verify cascading deletes (should return no rows)
SELECT * FROM poc.scenario_geographic_coverage
WHERE scenario_id = (SELECT id FROM poc.scenarios WHERE name = 'Test Scenario');

SELECT * FROM poc.scenario_sector_coverage
WHERE scenario_id = (SELECT id FROM poc.scenarios WHERE name = 'Test Scenario');

-- Delete an organization (should fail if referenced by a scenario)
DELETE FROM poc.organizations
WHERE name = 'Updated Test Organization';
