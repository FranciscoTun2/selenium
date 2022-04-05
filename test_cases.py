from settings import settings
class test_cases:
  strings = [
    "El melón",
    "El melon",
    "La sandia",
    "La sandía",
    "El negro",
  ]

  NFT = {
    "ERICK":[settings.HOST+"/nft?address=0x3f9fBB08B88B2E02901866b7D6C07A687ab39503&token_id=526"],
    "DANIEL":[settings.HOST+"/nft?address=0x3f9fBB08B88B2E02901866b7D6C07A687ab39503&token_id=325"],
    "ARTURO":[settings.HOST+"/nft?address=0x3f9fBB08B88B2E02901866b7D6C07A687ab39503&token_id=57",
              settings.HOST+"/nft?address=0x3f9fBB08B88B2E02901866b7D6C07A687ab39503&token_id=109",
              settings.HOST+"/nft?address=0x3f9fBB08B88B2E02901866b7D6C07A687ab39503&token_id=160"]
  }

  NFT_STRINGS = {
    "ERICK":["Las Jaras"],
    "DANIEL":["La Mano"],
    "ARTURO":["El Cazo", "La Araña", "La Corona"]
  }