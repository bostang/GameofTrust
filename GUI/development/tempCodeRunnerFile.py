json')
                    for user in data:
                        if user['id'] == rooms[room_index][1]:
                            user['coin'] += result1
                        elif user['id'] == rooms[room_index][2]:
                            user['coin'] += result2
                    write_to_json_file('database.json', data) 