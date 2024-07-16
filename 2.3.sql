SELECT
    endpoints.id,
    endpoints.name AS [Активное оборудование],
    COUNT(reasons.reason_name) AS [Количество причин простоя "Перебои напряжения"]
FROM
    endpoints,
    endpoint_reasons AS reasons
WHERE
    endpoints.active = 'true'
    AND reasons.endpoint_id = endpoints.id
    AND reasons.reason_name = 'Перебои напряжения'
GROUP BY
    reasons.endpoint_id;