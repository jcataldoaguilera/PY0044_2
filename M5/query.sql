SELECT
    LEG0.M_TRADE_NUM AS M_TRADE_NUM,
    KY.M_OBJ_ALT AS CALYPSO_ID,
    LEG0.M_TYPOLOGY AS M_TRADE_TYP,
    LEG0.M_PORTFOLIO AS PORTFOLIO,
    CASE
        WHEN TRIM(PAYLEG.M_PAY_CUR) = '' THEN RECLEG.M_PAY_CUR
        ELSE PAYLEG.M_PAY_CUR
    END AS SET_PAY_CUR,
    CASE
        WHEN TRIM(RECLEG.M_PAY_CUR) = '' THEN PAYLEG.M_PAY_CUR
        ELSE RECLEG.M_PAY_CUR
    END AS SET_REC_CUR,
    TO_CHAR(LEG0.M_HORIZON, 'dd-mm-yyyy') AS VALDATETIME,
    LEG0.M_NOTIONAL AS NOTIONAL,
    LEG0.M_NOTIONAL1 AS NOTIONAL_CUR,
    LEG0.M_NPV_PL AS MARKET_VALUE,
    LEG0.M_PL_CUR AS MARKET_VALUE_CUR,
    LEG0.M_NPV_PL AS BOOK_VALUE,
    LEG0.M_PL_CUR AS BOOK_VALUE_CUR,
    (
        COALESCE(NULLIF(LEG0.M_NPV_CLP, 0), 1) * COALESCE(NULLIF(PAYLEG.SPOT_PAY, 0), 1)
    ) AS NPV_PAY,
    PAYLEG.NPV_PAYLEG_CUR AS NPV_PAY_CUR,
    (
        COALESCE(NULLIF(LEG0.M_NPV_CLP, 0), 1) * COALESCE(NULLIF(RECLEG.SPOT_REC, 0), 1)
    ) AS NPV_REC,
    RECLEG.NPV_RECLEG_CUR AS NPV_REC_CUR,
    (
        (
            COALESCE(NULLIF(LEG0.M_NPV_CLP, 0), 1) -(ACCRUAL_PAYLEG_CLP + ACCRUAL_RECLEG_CLP)
        ) * COALESCE(NULLIF(PAYLEG.SPOT_PAY, 0), 1)
    ) AS NPV_NET_PAY,
    PAYLEG.NPV_PAYLEG_CUR AS NPV_NET_PAY_CUR,
    (
        (
            COALESCE(NULLIF(LEG0.M_NPV_CLP, 0), 1) -(ACCRUAL_PAYLEG_CLP + ACCRUAL_RECLEG_CLP)
        ) * COALESCE(NULLIF(RECLEG.SPOT_REC, 0), 1)
    ) AS NPV_NET_REC,
    RECLEG.NPV_RECLEG_CUR AS NPV_NET_REC_CUR,
    LEG0.M_NPV_CLP AS NPV_CLP,
    'CLP' AS NPV_CLP_CUR,
    LEG0.M_NPV_CLP AS PV_CLP,
    'CLP' AS PV_CLP_CUR,
    LEG0.M_NOTIONAL_ AS BCI_CLF_TO_BASE,
    'CLP' AS BCI_CLF_TO_BASE_CUR,
    PAYLEG.NPV_PAYLEG AS NPV_PAYLEG,
    PAYLEG.NPV_PAYLEG_CUR AS NPV_PAYLEG_CUR,
    PAYLEG.ACCRUAL_PAYLEG AS ACCRUAL_PAYLEG,
    PAYLEG.ACCRUAL_PAYLEG_CUR AS ACCRUAL_PAYLEG_CUR,
    PAYLEG.BCI_CLF_TO_BASE_PAY AS BCI_CLF_TO_BASE_PAY,
    PAYLEG.BCI_CLF_TO_BASE_PAY_CUR AS BCI_CLF_TO_BASE_PAY_CUR,
    RECLEG.NPV_RECLEG AS NPV_RECLEG,
    RECLEG.NPV_RECLEG_CUR AS NPV_RECLEG_CUR,
    RECLEG.ACCRUAL_RECLEG AS ACCRUAL_RECLEG,
    RECLEG.ACCRUAL_RECLEG_CUR AS ACCRUAL_RECLEG_CUR,
    RECLEG.BCI_CLF_TO_BASE_REC AS BCI_CLF_TO_BASE_REC,
    RECLEG.BCI_CLF_TO_BASE_REC_CUR AS BCI_CLF_TO_BASE_REC_CUR,
    CASE
        PAYLEG.M_LEG_ID
        WHEN 1 THEN CASE
            LEG0.M_RATE_TYPE
            WHEN 'Fixed' THEN 0.01 * (
                LEG0.M_RATE_1 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(PAYLEG.BPV, 0), 1)
                ) / 100
            )
            ELSE 0.01 * (
                LEG0.M_MARGIN_1 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(PAYLEG.BPV, 0), 1)
                ) / 100
            )
        END
        ELSE CASE
            LEG0.M_RATE_TYP1
            WHEN 'Fixed' THEN 0.01 * (
                LEG0.M_RATE_2 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(PAYLEG.BPV, 0), 1)
                ) / 100
            )
            ELSE 0.01 * (
                LEG0.M_MARGIN_2 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(PAYLEG.BPV, 0), 1)
                ) / 100
            )
        END
    END AS BREAK_EVEN_RATE_PAYLEG,
    PAYLEG.M_LEG_CUR AS BREAK_EVEN_RATE_PAYLEG_CUR,
    CASE
        RECLEG.M_LEG_ID
        WHEN 1 THEN CASE
            LEG0.M_RATE_TYPE
            WHEN 'Fixed' THEN 0.01 * (
                LEG0.M_RATE_1 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(RECLEG.BPV, 0), 1)
                ) / 100
            )
            ELSE 0.01 * (
                LEG0.M_MARGIN_1 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(RECLEG.BPV, 0), 1)
                ) / 100
            )
        END
        ELSE CASE
            LEG0.M_RATE_TYP1
            WHEN 'Fixed' THEN 0.01 * (
                LEG0.M_RATE_2 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(RECLEG.BPV, 0), 1)
                ) / 100
            )
            ELSE 0.01 * (
                LEG0.M_MARGIN_2 -(
                    LEG0.M_NPV_CLP / COALESCE(NULLIF(RECLEG.BPV, 0), 1)
                ) / 100
            )
        END
    END AS BREAK_EVEN_RATE_RECLEG,
    RECLEG.M_LEG_CUR AS BREAK_EVEN_RATE_RECLEG_CUR,
    0 AS MODIFIED_DURATION,
    LEG0.M_PL_CUR AS MODIFIED_DURATION_CUR
FROM
    DM_PM_SWAPS_REP LEG0,
    DM_KEYMAP_REP KY,
    (
        SELECT
            M_TRADE_NUM,
            M_REF_DATA,
            M_LEG_ID,
            M_LEG_CUR,
            M_PAY_CUR,
            DECODE(
                M_LEG_ID,
                1,
                M_BPV_1,
                2,
                M_BPV_2
            ) AS BPV,
            M_SPOT_CLP_ AS SPOT_PAY,
            M_NPV_LEG AS NPV_PAYLEG,
            M_LEG_CUR AS NPV_PAYLEG_CUR,
            M_ACCRUAL_1 AS ACCRUAL_PAYLEG_CLP,
            M_ACCRUAL AS ACCRUAL_PAYLEG,
            COALESCE(TRIM(M_ACCRUAL_C), TRIM(M_LEG_CUR)) AS ACCRUAL_PAYLEG_CUR,
            (-1.0 * M_LEG_NOMI1) AS BCI_CLF_TO_BASE_PAY,
            'CLP' AS BCI_CLF_TO_BASE_PAY_CUR
        FROM
            DM_PM_SWAPS_REP
        WHERE
            M_LEG_ID <> 0
            AND M_PAY_RECEI = 'PAY'
    ) PAYLEG,
    (
        SELECT
            M_TRADE_NUM,
            M_REF_DATA,
            M_LEG_ID,
            M_LEG_CUR,
            M_PAY_CUR,
            DECODE(
                M_LEG_ID,
                1,
                M_BPV_1,
                2,
                M_BPV_2
            ) AS BPV,
            M_SPOT_CLP_ AS SPOT_REC,
            M_NPV_LEG AS NPV_RECLEG,
            M_LEG_CUR AS NPV_RECLEG_CUR,
            M_ACCRUAL_1 AS ACCRUAL_RECLEG_CLP,
            M_ACCRUAL AS ACCRUAL_RECLEG,
            COALESCE(TRIM(M_ACCRUAL_C), TRIM(M_LEG_CUR)) AS ACCRUAL_RECLEG_CUR,
            M_LEG_NOMI1 AS BCI_CLF_TO_BASE_REC,
            'CLP' AS BCI_CLF_TO_BASE_REC_CUR
        FROM
            DM_PM_SWAPS_REP
        WHERE
            M_LEG_ID <> 0
            AND M_PAY_RECEI <> 'PAY'
    ) RECLEG
WHERE
    LEG0.M_LEG_ID = 0
    AND LEG0.M_CONTRACT_ (+) = KY.M_OBJ_ID
    AND TRIM(KY.M_OBJ_ASYS) IN ('Calypso')
    AND KY.M_OBJ_ALT <> '-1'
    AND LEG0.M_TRADE_NUM = PAYLEG.M_TRADE_NUM
    AND LEG0.M_TRADE_NUM = RECLEG.M_TRADE_NUM
    AND LEG0.M_REF_DATA = PAYLEG.M_REF_DATA
    AND LEG0.M_REF_DATA = RECLEG.M_REF_DATA
    AND (
        LEG0.M_STATUS = 'ToBeMatched'
        or LEG0.M_STATUS = 'Cleared'
    )
    AND LEG0.M_REF_DATA = 2849
    AND LEG0.M_TRADE_NUM = 28813