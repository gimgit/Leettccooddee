class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_room = set()
        def open_door(room):
            visited_room.add(room)
            for room in rooms[room]:
                if room not in visited_room:
                    open_door(room)

        open_door(0)
        return len(visited_room) == len(rooms)