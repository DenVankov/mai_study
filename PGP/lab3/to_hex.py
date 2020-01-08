# hex_dim = [0x03000000, 0x03000000]

hex_data_1 = [
    0x01000000, 0x05000000,
    0x00000000,
    0x00000000,
    0x64646400,
    0x00000000,
    0x00000000
]
hex_data_2 = [
    0x03000000, 0x03000000,
    0x00010200, 0x03040500, 0x06070800,
    0x08070600, 0x05040300, 0x02010000,
    0x00000000, 0x00140000, 0x00000000,
]

hex_data_3 = [
    0x03000000, 0x03000000,
    0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0xFFFFFF00, 0x00000000,
    0x00000000, 0x00000000, 0x00000000,
]

hex_data_4 = [
    0x03000000, 0x03000000,
    0xA2DF4C00, 0xF7C9FE00, 0x9ED84500,
    0xB4E85300, 0x99D14D00, 0x92DD5600,
    0xA9E04C00, 0xF7D1FA00, 0xD4D0E900,
]

hex_data_5 = [
    0x08000000, 0x08000000,
    0xD2E27502, 0xCFF65201, 0xD3ED5701, 0xD6E76902,
    0xC8F35B01, 0x8E168200, 0xCFF45001, 0xAE977604,
    0xD3DC7102, 0x7D1E7B00, 0xAB9A8004, 0xD9E58602,
    0xAB967E04, 0xAE9D8004, 0x87058200, 0xD0F95B01,
    0x74148000, 0xD0F55901, 0x86136C00, 0x85077400,
    0xD6E27702, 0xD3609F03, 0xD1609F03, 0xCC5EA103,
    0xCC739D03, 0x7C127F00, 0xAA988804, 0xAFA07D04,
    0xD0E37702, 0x7D117A00, 0xD6EB5901, 0xD6E37C02,
    0xC9F85701, 0xD655A103, 0xD7EA7402, 0x93127D00,
    0xD35BA403, 0xD4DD7902, 0xB0A18404, 0xD6DE7502,
    0xD765A900, 0xAD928404, 0xD0D87C02, 0xD7E97F02,
    0xCD509E00, 0xCAF85201, 0xCFF75601, 0xCEF45E01,
    0xD0E86902, 0xD1D17F02, 0xAD928104, 0xAFA18304,
    0xD4DB5C02, 0x88077D00, 0xC6F75701, 0x7D127D00,
    0xA99A8E04, 0xC8609E03, 0xD15DA503, 0xAB957E04,
    0xAE9A8004, 0x79218100, 0xD065A103, 0xA99E9A04,
]


with open('in.data', 'wb') as file:
    for val in hex_data_5:
        file.write(val.to_bytes(4, byteorder='big'))