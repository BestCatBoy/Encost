SELECT
    [groups].id,
    [groups].name AS [Неактивная точка],
    COUNT(reasons.reason_name) AS [Количество причин простоя]
FROM
    endpoints,
    endpoint_reasons AS reasons,
    endpoint_groups AS [groups]
WHERE
    [groups].endpoint_id = endpoints.id
    AND [groups].endpoint_id = reasons.endpoint_id AND 
    endpoints.active = 'false'
GROUP BY
    reasons.endpoint_id;