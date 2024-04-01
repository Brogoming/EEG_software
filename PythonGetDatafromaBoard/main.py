import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets, IpProtocolTypes


def main():
    BoardShim.enable_dev_board_logger()

    params = BrainFlowInputParams()
    params.serial_port = "COM4"
    board_id = BoardIds.CYTON_DAISY_BOARD.value

    board = BoardShim(board_id, params)
    board.prepare_session()
    board.start_stream ()
    time.sleep(10)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    board.stop_stream()
    board.release_session()

    print(data)


if __name__ == "__main__":
    main()