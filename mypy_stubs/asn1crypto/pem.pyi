from typing import Optional, Dict, Tuple

def armor(type_name: str, der_bytes: bytes, headers: Optional[Dict[str, str]] = None) -> bytes: ...
def unarmor(pem_bytes: bytes , multiple: bool = False) -> Tuple[str, Dict[str, str], bytes]: ...
