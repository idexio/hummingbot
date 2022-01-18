from hummingbot.client.config.config_var import ConfigVar
from hummingbot.client.config.config_methods import using_exchange
from hummingbot.core.event.events import OrderType, TradeType
from hummingbot.core.utils.tracking_nonce import get_tracking_nonce


EXAMPLE_PAIR = "IDEX-USD"
DEFAULT_FEES = [0.1, 0.25]  # fees in percentage for maker, taker
GAS_EXTRA_FEES = [0, 0.25]  # extra fee in percentage to account for gas costs (this is a very gross approximation)

ETH_GAS_LIMIT = 170000  # estimation of upper limit of gas idex uses to move its smart contact for each fill
BSC_GAS_LIMIT = 60000  # estimate from real taker orders
MATIC_GAS_LIMIT = 285000  # estimate from real taker orders


# --- users should not modify anything beyond this point ---

EXCHANGE_NAME = "idex"
HBOT_BROKER_ID = "HBOT-"
IDEX_BLOCKCHAINS = ('MATIC', )


def validate_idex_contract_blockchain(value: str) -> bool:
    if value not in IDEX_BLOCKCHAINS:
        raise Exception(f'Value {value} must be one of: {IDEX_BLOCKCHAINS}')
    return True


def get_gas_limit(blockchain: str) -> int:
    blockchain = str(blockchain).upper()
    try:
        gas_limit = globals()[f'{blockchain}_GAS_LIMIT']
    except KeyError:
        gas_limit = MATIC_GAS_LIMIT
    return gas_limit


# Example: HBOT-B-DIL-ETH-64106538-8b61-11eb-b2bb-1e29c0300f46
def get_new_client_order_id(is_buy: bool, trading_pair: str) -> str:
    side = "B" if is_buy else "S"
    return f"{HBOT_BROKER_ID}{side}-{trading_pair}-{get_tracking_nonce()}"


HB_ORDER_TYPE_TO_IDEX_PARAM_MAP = {
    OrderType.MARKET: "market",
    OrderType.LIMIT: "limit",
    OrderType.LIMIT_MAKER: "limitMaker",
}


def hb_order_type_to_idex_param(order_type: OrderType):
    return HB_ORDER_TYPE_TO_IDEX_PARAM_MAP[order_type]


HB_TRADE_TYPE_TO_IDEX_PARAM_MAP = {
    TradeType.BUY: "buy",
    TradeType.SELL: "sell",
}


def hb_trade_type_to_idex_param(trade_type: TradeType):
    return HB_TRADE_TYPE_TO_IDEX_PARAM_MAP[trade_type]


IDEX_PARAM_TO_HB_ORDER_TYPE_MAP = {
    "market": OrderType.MARKET,
    "limit": OrderType.LIMIT,
    "limitMaker": OrderType.LIMIT_MAKER,
}


def idex_param_to_hb_order_type(order_type: str) -> OrderType:
    return IDEX_PARAM_TO_HB_ORDER_TYPE_MAP[order_type]


IDEX_PARAM_TO_HB_TRADE_TYPE_MAP = {
    "buy": TradeType.BUY,
    "sell": TradeType.SELL,
}


def idex_param_to_hb_trade_type(side: str) -> TradeType:
    return IDEX_PARAM_TO_HB_TRADE_TYPE_MAP[side]


KEYS = {
    "idex_api_key":
        ConfigVar(key="idex_api_key",
                  prompt="Enter your IDEX API key (smart contract blockchain: MATIC) >>> ",
                  required_if=using_exchange(EXCHANGE_NAME),
                  is_secure=True,
                  is_connect_key=True),
    "idex_api_secret_key":
        ConfigVar(key="idex_api_secret_key",
                  prompt="Enter your IDEX API secret key>>> ",
                  required_if=using_exchange(EXCHANGE_NAME),
                  is_secure=True,
                  is_connect_key=True),
    "idex_wallet_private_key":
        ConfigVar(key="idex_wallet_private_key",
                  prompt="Enter your wallet private key>>> ",
                  required_if=using_exchange(EXCHANGE_NAME),
                  is_secure=True,
                  is_connect_key=True),
}


OTHER_DOMAINS = ["idex_sandbox_matic"]
OTHER_DOMAINS_PARAMETER = {  # will be passed as argument "domain" to the exchange class
    "idex_sandbox_matic": "sandbox_matic",
}
OTHER_DOMAINS_EXAMPLE_PAIR = {"idex_sandbox_matic": "IDEX-USD"}
OTHER_DOMAINS_DEFAULT_FEES = {"idex_sandbox_matic": [0.1, 0.25]}
OTHER_DOMAINS_KEYS = {
    "idex_sandbox_matic": {
        "idex_sandbox_matic_api_key":
            ConfigVar(key="idex_sandbox_matic_api_key",
                      prompt="Enter your IDEX API key ([sandbox] smart contract blockchain: MATIC) >>> ",
                      required_if=using_exchange("idex_sandbox_matic"),
                      is_secure=True,
                      is_connect_key=True),
        "idex_sandbox_matic_api_secret_key":
            ConfigVar(key="idex_sandbox_matic_api_secret_key",
                      prompt="Enter your IDEX API secret key>>> ",
                      required_if=using_exchange("idex_sandbox_matic"),
                      is_secure=True,
                      is_connect_key=True),
        "idex_sandbox_matic_wallet_private_key":
            ConfigVar(key="idex_sandbox_matic_wallet_private_key",
                      prompt="Enter your wallet private key>>> ",
                      required_if=using_exchange("idex_sandbox_matic"),
                      is_secure=True,
                      is_connect_key=True),
    },
}


DEBUG = False

DISABLE_LISTEN_FOR_ORDERBOOK_DIFFS = True

ORDER_BOOK_SNAPSHOT_REFRESH_TIME = 180
