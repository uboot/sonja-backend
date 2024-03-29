from fastapi import APIRouter, Depends, HTTPException, status
from public.auth import get_read, get_write
from public.schemas.channel import ChannelReadItem, ChannelWriteItem
from public.crud.channel import create_channel, delete_channel, read_channel, update_channel
from sonja.database import get_session, Session

router = APIRouter()


@router.post("/channel", response_model=ChannelReadItem, response_model_by_alias=False,
             status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_write)])
def post_channel_item(channel: ChannelWriteItem, session: Session = Depends(get_session)):
    new_channel = create_channel(session, channel)
    return ChannelReadItem.from_db(new_channel)


@router.get("/channel/{channel_id}", response_model=ChannelReadItem, response_model_by_alias=False,
            dependencies=[Depends(get_read)])
def get_channel_item(channel_id: str, session: Session = Depends(get_session)):
    channel = read_channel(session, channel_id)
    if channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    return ChannelReadItem.from_db(channel)


@router.patch("/channel/{channel_id}", response_model=ChannelReadItem, response_model_by_alias=False,
              dependencies=[Depends(get_write)])
def get_channel_item(channel_id: str, channel_item: ChannelWriteItem, session: Session = Depends(get_session)):
    channel = read_channel(session, channel_id)
    if channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    patched_channel = update_channel(session, channel, channel_item)
    t = ChannelReadItem.from_db(patched_channel)
    return t


@router.delete("/channel/{channel_id}", dependencies=[Depends(get_write)])
def delete_channel_item(channel_id: str, session: Session = Depends(get_session)):
    channel = read_channel(session, channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    delete_channel(session, channel)
