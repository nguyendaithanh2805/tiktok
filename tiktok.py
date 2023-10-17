
import base64

# Đoạn mã giải mã
encoded_data = '''
aW1wb3J0IHJlcXVlc3RzLCBvcw0KaW1wb3J0IHJlcXVlc3RzLCBqc29uLCB0aW1lLCBkYXRldGltZSwgcmUNCmNsYXNzIE9PUDoNCiAgICBkZWYgX19pbml0X18oc2VsZiwgVERTX3Rva2VuLCBpZHRpa3Rvayk6DQogICAgICAgIHNlbGYuVERTX3Rva2VuID0gVERTX3Rva2VuDQogICAgICAgIHNlbGYuaWR0aWt0b2sgPSBpZHRpa3Rvaw0KICAgICAgICBzZWxmLmRlbU5WID0gMA0KICAgICAgICBzZWxmLnh1SGllblRhaSA9IDANCiAgICAgICAgc2VsZi5TVFQgPSAwDQogICAgICAgIHNlbGYucyA9IHJlcXVlc3RzLlNlc3Npb24oKQ0KICAgIGRlZiBsYXlUaG9uZ1RpbkFjYyhzZWxmKToNCiAgICAgICAgdXJsID0gJ2h0dHBzOi8vdHJhb2RvaXN1Yi5jb20vYXBpLz9maWVsZHM9cHJvZmlsZSZhY2Nlc3NfdG9rZW49ezB9Jy5mb3JtYXQoc2VsZi5URFNfdG9rZW4pDQogICAgICAgIHJlc3BvbnNlID0gc2VsZi5zLmdldCh1cmwpDQogICAgICAgIGRhdGFMVFQgPSAganNvbi5sb2FkcyhyZXNwb25zZS50ZXh0KQ0KICAgICAgICBpZignZXJyb3InIGluIGRhdGFMVFQpOg0KICAgICAgICAgICAgcHJpbnQoJ1Rva2VuIHRkcyBkaWUgISEhJykNCiAgICAgICAgICAgIGV4aXQoKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgdXNlciA9IGRhdGFMVFRbJ2RhdGEnXVsndXNlciddDQogICAgICAgICAgICB4dSA9IGRhdGFMVFRbJ2RhdGEnXVsneHUnXQ0KICAgICAgICAgICAgeHVkaWUgPSBkYXRhTFRUWydkYXRhJ11bJ3h1ZGllJ10NCiAgICAgICAgICAgIHNlbGYueHVIaWVuVGFpICs9IGludCh4dSkNCiAgICAgICAgICAgIHByaW50KGYnVXNlciA6IHt1c2VyfSB8IFh1IDoge3h1fSB8IFh1IGRpZSA6IHt4dWRpZX0nKQ0KICAgIGRlZiBkYXRDYXVIaW5oKHNlbGYpOg0KICAgICAgICB1cmwgPSAnaHR0cHM6Ly90cmFvZG9pc3ViLmNvbS9hcGkvP2ZpZWxkcz10aWt0b2tfcnVuJmlkPXswfSZhY2Nlc3NfdG9rZW49ezF9Jy5mb3JtYXQoc2VsZi5pZHRpa3Rvaywgc2VsZi5URFNfdG9rZW4pDQogICAgICAgIHJlc3BvbnNlID0gc2VsZi5zLmdldCh1cmwpDQogICAgICAgIGRhdGFEQ0ggPSBqc29uLmxvYWRzKHJlc3BvbnNlLnRleHQpDQogICAgICAgIGlmKCdlcnJvcicgaW4gZGF0YURDSCk6DQogICAgICAgICAgICBwcmludCgnS2nhu4NtIHRyYSBs4bqhaSB4ZW0gY+G6pXUgaMOsbmggdGlrdG9rIGNoxrBhJykNCiAgICAgICAgICAgIGV4aXQoKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgaWQgPSBkYXRhRENIWydkYXRhJ11bJ2lkJ10NCiAgICAgICAgICAgIHVzZXIgPSBkYXRhRENIWydkYXRhJ11bJ3VuaXF1ZUlEJ10NCiAgICAgICAgICAgIG1zZyA9IGRhdGFEQ0hbJ2RhdGEnXVsnbXNnJ10NCiAgICAgICAgICAgIHByaW50KGYne2lkfSB8IHt1c2VyfSB8IHttc2d9JykNCiAgICBkZWYgbGF5TmhpZW1WdShzZWxmKToNCiAgICAgICAgd2hpbGUoVHJ1ZSk6DQogICAgICAgICAgICB1cmwgPSAnaHR0cHM6Ly90cmFvZG9pc3ViLmNvbS9hcGkvP2ZpZWxkcz10aWt0b2tfZm9sbG93JmFjY2Vzc190b2tlbj17fScuZm9ybWF0KHNlbGYuVERTX3Rva2VuKQ0KICAgICAgICAgICAgcmVzcG9uc2UgPSBzZWxmLnMuZ2V0KHVybCkNCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICBkYXRhID0ganNvbi5sb2FkcyhyZXNwb25zZS50ZXh0KQ0KICAgICAgICAgICAgICAgIGlmICdjb3VudGRvd24nIGluIGRhdGE6DQogICAgICAgICAgICAgICAgICAgICAgICBjb3VudGRvd25fdmFsdWUgPSBkYXRhWydjb3VudGRvd24nXQ0KICAgICAgICAgICAgICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoaW50KGNvdW50ZG93bl92YWx1ZSkgKyA1LCAwLCAtMSk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZidUaGFvIHTDoWMgcXXDoSBuaGFuaCB2dWkgbMOybmcgY2jhuq1tIGzhuqFpLCDEkeG7o2kge2l9IGdpw6J5JywgZW5kPSdccicpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgdGltZS5zbGVlcCgxKQ0KICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoIiAiICogNTAsIGVuZD0nXHInKQ0KICAgICAgICAgICAgICAgIGVsaWYgJ3RpbWVfcmVzZXQnIGluIGRhdGE6DQogICAgICAgICAgICAgICAgICAgIHByaW50KCfEkOG7lWkgdGlrdG9rIG3hu5tpLCBi4buLIGdp4bubaSBo4bqhbiBuaGnhu4dtIHbhu6UgcuG7k2knKQ0KICAgICAgICAgICAgICAgICAgICBleGl0KCkNCiAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICBmb3IgaXRlbSBpbiBkYXRhWydkYXRhJ106DQogICAgICAgICAgICAgICAgICAgICAgICBsaW5rX3ZhbHVlID0gaXRlbVsnbGluayddDQogICAgICAgICAgICAgICAgICAgICAgICBpZF92YWx1ZSA9IGl0ZW1bJ2lkJ10NCiAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYuZ3VpTmhpZW1WdShpZF92YWx1ZSkNCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIChzZWxmLlNUVCA9PSBhbnN3ZXIpOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYubmdoaUNob25nQmxvY2soY2hvbmdCbG9jaykNCiAgICAgICAgICAgICAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgc2VsZi5kZWxheShzZWNvbmRzKQ0KICAgICAgICAgICAgICAgICAgICAgICAgc2VsZi5mb2xsb3cobGlua192YWx1ZSkNCiAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYuZGVtTlYgKz0gMQ0KICAgICAgICAgICAgICAgICAgICAgICAgaWYgc2VsZi5kZW1OViA9PSA5Og0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNlbGYubmhhblh1KCkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBzZWxmLmRlbU5WID0gMA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlDQogICAgICAgICAgICAgICAgICAgICAgICAjIGZvciBpIGluIHJhbmdlKGxlbihhcnJfbGlua192YWx1ZSkpOg0KICAgICAgICAgICAgICAgICAgICAgICAgIyAgICAgbGlua192YWx1ZSA9IGFycl9saW5rX3ZhbHVlW2ldDQogICAgICAgICAgICAgICAgICAgICAgICAjICAgICBwcmludChsaW5rX3ZhbHVlKQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgaWRfdmFsdWUgPSBhcnJfaWRfdmFsdWVbaV0NCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIHNlbGYuZ3VpTmhpZW1WdShpZF92YWx1ZSkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIHRpbWUuc2xlZXAoNSkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAjIHNlbGYuZm9sbG93KGxpbmtfdmFsdWUpDQoNCiAgICAgICAgICAgIGV4Y2VwdCBqc29uLkpTT05EZWNvZGVFcnJvcjoNCiAgICAgICAgICAgICAgICBwcmludCgiRXJyb3IgZGVjb2RpbmcgSlNPTiByZXNwb25zZS4iKQ0KICAgIGRlZiBndWlOaGllbVZ1KHNlbGYsIGlkX3ZhbHVlKToNCiAgICAgICAgdXJsID0gJ2h0dHBzOi8vdHJhb2RvaXN1Yi5jb20vYXBpL2NvaW4vP3R5cGU9VElLVE9LX0ZPTExPV19DQUNIRSZpZD17MH0mYWNjZXNzX3Rva2VuPXsxfScuZm9ybWF0KGlkX3ZhbHVlLCBzZWxmLlREU190b2tlbikNCiAgICAgICAgcmVzcG9uc2UgPSBzZWxmLnMuZ2V0KHVybCkNCiAgICAgICAgZGF0YUdOViA9IHJlc3BvbnNlLmpzb24oKQ0KICAgICAgICANCiAgICAgICAgIyBmb3IgaSBpbiByYW5nZSgxLCBkYXRhR05WWydjYWNoZSddICsgMSk6DQogICAgICAgICMgICAgIHNlbGYuZGVtTlYgKz0gMQ0KICAgICAgICAjICAgICBpZiBzZWxmLmRlbU5WID09IDk6DQogICAgICAgICMgICAgICAgICBzZWxmLm5oYW5YdSgpDQogICAgICAgICMgICAgICAgICBzZWxmLmRlbU5WID0gMA0KICAgICAgICAjICAgICAgICAgY29udGludWUNCiAgICBkZWYgZm9sbG93KHNlbGYsIGxpbmtfdmFsdWUpOg0KICAgICAgIG9zLnN5c3RlbShmJ3Rlcm11eC1vcGVuLXVybCB7bGlua192YWx1ZX0nKQ0KICAgIGRlZiBuaGFuWHUoc2VsZik6DQogICAgICAgIHRyeToNCiAgICAgICAgICAgIG5vdyA9IGRhdGV0aW1lLmRhdGV0aW1lLm5vdygpDQogICAgICAgICAgICB1cmwgPSAnaHR0cHM6Ly90cmFvZG9pc3ViLmNvbS9hcGkvY29pbi8/dHlwZT1USUtUT0tfRk9MTE9XJmlkPVRJS1RPS19GT0xMT1dfQVBJJmFjY2Vzc190b2tlbj17fScuZm9ybWF0KHNlbGYuVERTX3Rva2VuKQ0KICAgICAgICAgICAgcmVzcG9uc2UgPSBzZWxmLnMuZ2V0KHVybCkNCiAgICAgICAgICAgIGRhdGFOWCA9IHJlc3BvbnNlLmpzb24oKQ0KICAgICAgICAgICAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0KICAgICAgICAgICAgICAgIGlmICdkYXRhJyBpbiBkYXRhTlg6DQogICAgICAgICAgICAgICAgICAgIHh1ID0gZGF0YU5YWydkYXRhJ11bJ3h1J10NCiAgICAgICAgICAgICAgICAgICAgam9iX3N1Y2Nlc3MgPSBkYXRhTlhbJ2RhdGEnXVsnam9iX3N1Y2Nlc3MnXQ0KICAgICAgICAgICAgICAgICAgICAjIHh1dGhlbSA9IGRhdGFOWFsnZGF0YSddWyd4dV90aGVtJ10NCiAgICAgICAgICAgICAgICAgICAgbXNnID0gZGF0YU5YWydkYXRhJ11bJ21zZyddDQogICAgICAgICAgICAgICAgICAgIHh1VG9uZyA9IGludChyZS5zZWFyY2gocidcZCsnLCB4dSkuZ3JvdXAoKSkNCiAgICAgICAgICAgICAgICAgICAgc2VsZi54dUhpZW5UYWkgKz0geHVUb25nDQogICAgICAgICAgICAgICAgICAgIHNlbGYuU1RUKz0gMQ0KICAgICAgICAgICAgICAgICAgICBwcmludChmIlt7c2VsZi5TVFR9XSB8IHtub3cuc3RyZnRpbWUoJyVIOiVNOiVTJyl9IHwgIFPhu5Egam9iIMSRw6MgbMOgbSA6IHtqb2Jfc3VjY2Vzc30gfCBUSMOATkggVE9PTCB8IHttc2d9IHwge3h1VG9uZ30gfCBYdSBoaeG7h24gdOG6oWkgOiB7c2VsZi54dUhpZW5UYWl9IikNCiAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICBwcmludCgiTmhhbiB4dSB0aGF0IGJhaSIpDQogICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgIHByaW50KGYiWcOqdSBj4bqndSBraMO0bmcgdGjDoG5oIGPDtG5nLiBNw6MgdHLhuqFuZyB0aMOhaToge3Jlc3BvbnNlLnN0YXR1c19jb2RlfSIpDQogICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgIHByaW50KCdOaGFuIHh1IGtob25nIGR1b2MgdmkgdGlrdG9rIGJpIG5oYSByb2knKQ0KICAgIGRlZiBkZWxheShzZWxmLCBzZWNvbmRzKToNCiAgICAgICAgZm9yIGkgaW4gcmFuZ2Uoc2Vjb25kcywgMCwgLTEpOg0KICAgICAgICAgICAgcHJpbnQoZidWdWkgbMOybmcgxJHhu6NpIHNhdSAtPiB7c3RyKGkpfSBnacOieScsIGVuZD0nXHInKQ0KICAgICAgICAgICAgdGltZS5zbGVlcCgxKQ0KICAgIGRlZiBuZ2hpQ2hvbmdCbG9jayhzZWxmLCBjaG9uZ0Jsb2NrKToNCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoY2hvbmdCbG9jaywgMCwgLTEpOg0KICAgICAgICAgICAgcHJpbnQoZifEkGFuZyBuZ2jhu4kgY2jhu5FuZyBibG9jaywgdnVpIGzDsm5nIMSR4bujaSBzYXUgLT4ge3N0cihpKX0gZ2nDonknLCBlbmQ9J1xyJykNCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMSkNCmRlZiBzYXZlX2FjY291bnRfaW5mbyhURFNfdG9rZW4sIGlkdGlrdG9rKToNCiAgICB3aXRoIG9wZW4oInRkc190b2tlbi50eHQiLCAidyIpIGFzIHRkc19maWxlOg0KICAgICAgICB0ZHNfZmlsZS53cml0ZShURFNfdG9rZW4pDQogICAgd2l0aCBvcGVuKCJpZHRpa3Rvay50eHQiLCAidyIpIGFzIGlkdGlrdG9rX2ZpbGU6DQogICAgICAgIGlkdGlrdG9rX2ZpbGUud3JpdGUoaWR0aWt0b2spDQoNCmRlZiBsb2FkX2FjY291bnRfaW5mbygpOg0KICAgIHRyeToNCiAgICAgICAgd2l0aCBvcGVuKCJ0ZHNfdG9rZW4udHh0IiwgInIiKSBhcyB0ZHNfZmlsZToNCiAgICAgICAgICAgIFREU190b2tlbiA9IHRkc19maWxlLnJlYWQoKQ0KICAgICAgICB3aXRoIG9wZW4oImlkdGlrdG9rLnR4dCIsICJyIikgYXMgaWR0aWt0b2tfZmlsZToNCiAgICAgICAgICAgIGlkdGlrdG9rID0gaWR0aWt0b2tfZmlsZS5yZWFkKCkNCiAgICAgICAgcmV0dXJuIFREU190b2tlbiwgaWR0aWt0b2sNCiAgICBleGNlcHQgRmlsZU5vdEZvdW5kRXJyb3I6DQogICAgICAgIHJldHVybiBOb25lLCBOb25lDQpURFNfdG9rZW4sIGlkdGlrdG9rID0gbG9hZF9hY2NvdW50X2luZm8oKQ0KaWYgVERTX3Rva2VuIGlzIE5vbmUgb3IgaWR0aWt0b2sgaXMgTm9uZToNCiAgICBURFNfdG9rZW4gPSBpbnB1dCgnTmjhuq1wIHRva2VuIFREUyA6ICcpDQogICAgaWR0aWt0b2sgPSBpbnB1dCgnTmjhuq1wIGlkIHRpa3RvayBj4bqnbiBj4bqldSBow6xuaCA6ICcpDQogICAgc2F2ZV9hY2NvdW50X2luZm8oVERTX3Rva2VuLCBpZHRpa3RvaykNCmVsc2U6DQogICAga2VlcF9vbGRfdG9rZW4gPSBpbnB1dCgnQuG6oW4gY8OzIG114buRbiBnaeG7ryBs4bqhaSB0b2tlbiBURFMgY8WpIGtow7RuZz8gKHkvbik6ICcpDQogICAgaWYga2VlcF9vbGRfdG9rZW4ubG93ZXIoKSAhPSAneSc6DQogICAgICAgIFREU190b2tlbiA9IGlucHV0KCdOaOG6rXAgdG9rZW4gVERTIG3hu5tpOiAnKQ0KDQogICAga2VlcF9vbGRfaWR0aWt0b2sgPSBpbnB1dCgnQuG6oW4gY8OzIG114buRbiBnaeG7ryBs4bqhaSBpZCB0aWt0b2sgY8WpIGtow7RuZz8gKHkvbik6ICcpDQogICAgaWYga2VlcF9vbGRfaWR0aWt0b2subG93ZXIoKSAhPSAneSc6DQogICAgICAgIGlkdGlrdG9rID0gaW5wdXQoJ05o4bqtcCBpZCB0aWt0b2sgbeG7m2k6ICcpDQogICAgc2F2ZV9hY2NvdW50X2luZm8oVERTX3Rva2VuLCBpZHRpa3RvaykNCnNlY29uZHMgPSBpbnQoaW5wdXQoJ05o4bqtcCBkZWxheSA6ICcpKQ0KYW5zd2VyID0gaW50KGlucHV0KCdTYXUgYmFvIG5oacOqdSBuaGnhu4dtIHbhu6UgdGjDrCBuZ2jhu4kgY2jhu5FuZyBibG9jayA6ICcpKQ0KY2hvbmdCbG9jayA9IGludChpbnB1dCgnTmdo4buJIGNo4buRbmcgYmxvY2sgYmFvIG5oacOqdSBnacOieSA6ICcpKQ0KIyBvcy5zeXN0ZW0oJ3Rlcm11eC1vcGVuLXVybCBodHRwczpcL1wvdGlrdG9rLmNvbVwvQG5ndXllbm5nb2NxdWFuZzAwNCcpDQojIFREU190b2tlbiA9ICdURFNRZmlramNsWlhaekppT2lJWFoyVjJjaXdpSXhFVE14Z21iaGhHZHBGR1ppb2pJeVYyYzFKeWUnDQojIGlkdGlrdG9rID0gJzcxNzA1Nzk2NDU3Mjc4Njc5MzEnDQphcGkgPSBPT1AoVERTX3Rva2VuLCBpZHRpa3RvaykNCmFwaS5kYXRDYXVIaW5oKCkNCmFwaS5sYXlOaGllbVZ1KCkNCg==
'''

# Giải mã và thực thi nội dung
exec(base64.b64decode(encoded_data).decode('utf-8'))
