SELECT
    reasons.reason_name AS [Причины простоя активных станков]
FROM
    endpoints,
    endpoint_reasons AS reasons
WHERE
    endpoints.active = 'true'
    AND reasons.endpoint_id = endpoints.id
GROUP BY
    reasons.reason_name;